#include<math.h>
#include<stdlib.h>
#include<stdio.h>

// #define NX 62
// #define NY 100
// #define NZ 14

#define NX 40
#define NY 40
#define NZ 40
#define NFREQS 3
#define NSTEPS 5000
#define NPML 7

void main()
{
	// VARIABLES
	int ia,ja,ka,ib,jb,kb,ic,jc,kc;
	int i,j,k,m,n;
	float ddx,dt,T,pi,e0,muz,ra_x,ra_y,courant;
	float t0,spread,pulse,f_peak;

	ia = 0;
	ja = 14;
	ka = 7;
	ib = NX - ia - 1;
	jb = NY - ja - 1;
	kb = NZ - ka - 1;
	ic = NX/2;
	jc = NY/2;
	kc = NZ/2;

	courant = 0.5;
	muz = 4*pi*1.e-7;
	ddx = 0.01;
	dt = ddx/6e8;
	e0 = 8.854e-12;
	pi = 3.14159;
	t0 = 20.0;
	spread = 6.0;
	T = 0;
	f_peak = .05;

	// FIELDS
	float gax[NX][NY][NZ], gay[NX][NY][NZ], gaz[NX][NY][NZ];
	float gbx[NX][NY][NZ], gby[NX][NY][NZ], gbz[NX][NY][NZ];
	float dx[NX][NY][NZ], dy[NX][NY][NZ], dz[NX][NY][NZ];
	float ex[NX][NY][NZ], ey[NX][NY][NZ], ez[NX][NY][NZ];
	float hx[NX][NY][NZ], hy[NX][NY][NZ], hz[NX][NY][NZ];
	float ix[NX][NY][NZ], iy[NX][NY][NZ], iz[NX][NY][NZ];
	float curl_h, curl_e;

	// TF/SF BUFFERS
	float idxl[ia][NY][NZ], idxh[ia][NY][NZ], ihxl[ia][NY][NZ], ihxh[ia][NY][NZ];
	float idyl[NX][ja][NZ], idyh[NX][ja][NZ], ihyl[NX][ja][NZ], ihyh[NX][ja][NZ];
	float idzl[NX][NY][ka], idzh[NX][NY][ka], ihzl[NX][NY][ka], ihzh[NX][NY][ka];
	int ixh, jyh, kzh;
	float xn,xxn;

	// PML PARAMETERS
	float gi1[NX],gi2[NX],gi3[NX],fi1[NX],fi2[NX],fi3[NX];
	float gj1[NY],gj2[NY],gj3[NY],fj1[NY],fj2[NY],fj3[NY];
	float gk1[NZ],gk2[NZ],gk3[NZ],fk1[NZ],fk2[NZ],fk3[NZ];

	// WAVE PROPOGATION BUFFERS
	float ez_inc[NY], hx_inc[NY];
	
	// FOURIER TRANSFORM ARRAYS
	float freq[NFREQS], arg[NFREQS];
	float real_pt[NFREQS][NX][NY],imag_pt[NFREQS][NX][NY];
	float ampl[NX][NY], phase[NX][NY];
	float real_in[NFREQS], imag_in[NFREQS], ampl_in[NFREQS], phase_in[NFREQS];

	// DIELECTRIC SPHERE PARAMETERS
	float dist, xdist, ydist, zdist;
	float radius, epsilon, sigma, epsilon_free, sigma_free, eps, cond, e_sub;

	// FILE I/0
	FILE *fp, *fp2, *shape_file, *source_file, *fopen();
	int pixel, shape[NX*NY*NZ], source[NX*NY*NZ];
	unsigned long it;
	char line[10];

	int use_shape = 1;

	ra_y = 0.6625;
	ra_x = 0.6812;
	e_sub = 2.2;

	int i_patch_st, i_patch_end, j_patch_st, j_patch_end, j_ref, kstart, kend, k_ref, istart, iend, ktop;
	float feed[NX][NZ], i_ref;
	int j_feed;

	printf("Hellow! World");

// *******************************
// ******* IMPORT GEOMETRY *******
// *******************************
	shape_file = fopen("shape.dat","r");
	while (fgets(line,10, shape_file) != NULL) {
		sscanf(line,"%d", &pixel);
		if (pixel < 256) {
			shape[it] = pixel;
			it++;
		}
	}
	fclose(shape_file);

	source_file = fopen("source.dat","r");
	while (fgets(line,10, source_file) != NULL) {
	 	sscanf(line,"%d", &pixel);
		if (pixel < 256) {
	 		source[it] = pixel;
	 		it++;
	 	}
	}
	fclose(source_file);

	for (k=0; k < NZ; k++) {
		for (j=0; j < NY; j++) {
			for (i=0; i < NX; i++) {
				ex[i][j][k] = 0.0;
				ey[i][j][k] = 0.0;
				ez[i][j][k] = 0.0;
				dx[i][j][k] = 0.0;
				dy[i][j][k] = 0.0;
				dz[i][j][k] = 0.0;
				hx[i][j][k] = 0.0;
				hy[i][j][k] = 0.0;
				hz[i][j][k] = 0.0;
				gax[i][j][k] = 1.0;
				gay[i][j][k] = 1.0;
				gaz[i][j][k] = 1.0;
				gbx[i][j][k] = 0.0;
				gby[i][j][k] = 0.0;
				gbz[i][j][k] = 0.0;
				feed[i][k] = 0.0;
			}
		}
	}

	freq[0] = 10.e6;
	freq[1] = 100.e6;
	freq[2] = 433.e6;

	for (n=0; n < NFREQS; n++) {
		arg[n] = 2*pi*freq[n]*dt;
		real_in[n] = 0.;
		imag_in[n] = 0.;
		for (j=0; j < NY; j++) {
			for (i = 0; i < NX; i++) {
				real_pt[n][i][j] = 0.;
				imag_pt[n][i][j] = 0.;
			}
		}
	}

	if (use_shape == 1) {
		// patch_antenna
		kstart = 0;
		kend = 2;
		istart = 20;
		iend = 24;

		// id_cap
		kstart = 13;
		kend =21;
		istart = 15;
		iend = 24;

		kstart = 2;
		kend = 2;
		istart = 24;
		iend = 34;
		j_feed = ja;

		it = 0;
		for (k=0; k < NZ; k++) {
			for (j=NY-1; j >= 0; j--) {
				for (i=0; i < NX; i++) {
					gax[i][j][k] = 1.-shape[it]/255.;
					gay[i][j][k] = 1.-shape[it]/255.;
					gaz[i][j][k] = 1.-shape[it]/255.;
					if (i <= iend && i >= istart) {
						if (k <= kend && k >= kstart) {
							feed[i][k] = 1.0;
						}
					}
					it++;
					printf("%d\t%d\t%d\t%d\t%f\n",i,j,k,shape[it],gax[i][j][k]);
				}
			}
		}
		for (j=1; j < NY-1; j++) {
		 	for (i=1; i < NX-1; i++) {
		 		gaz[i][j][0] = 116./255.;
		 	}
		}
		 printf("%d\t%d\t%d\t%d\t%d\n",j_feed,istart,iend,kstart,kend);

		it = 0;
		for (k=0; k < NZ; k++) {
		 	for (j=NY-1; j >= 0; j--) {
		 		for (i=0; i < NX; i++) {
		 			if (shape[it] == 0) {
		 				if (k <= 2) {
		 					gax[i][j][k] = 1./e_sub;
		 					gay[i][j][k] = 1./e_sub;
		 					gaz[i][j][k] = 1./e_sub;
		 				} else {
		 					gax[i][j][k] = 1.;
		 					gay[i][j][k] = 1.;
		 					gaz[i][j][k] = 1.;
		 				}
		 			} else if (shape[it] == 127) {
		 				gax[i][j][k] = 1./e_sub;
		 				gay[i][j][k] = 1./e_sub;
		 				gaz[i][j][k] = 1./e_sub;
		 				feed[i][k] = 1.;
		 				j_feed = j;
		 				if (k > kend) {
		 				 	kend = k;
		 				} else if (k < kstart) {
		 				 	kstart =k;
		 				}
		 				if (i > iend) {
		 				 	iend = i;
		 				} else if (i < istart) {
		 				 	istart = i;
		 				}
		 				printf("%d\t%d\t%d\n",i,j,k);
		 			} else if (shape[it] == 255) {
						gax[i][j][k] = 0.;
		 				gay[i][j][k] = 0.;
		 			}
		 			printf("%d\t%d\t%d\t%lu\t%d\n",i,j,k,it,shape[it]);
		 			it++;
		 		}
		 	}
		}
		printf("%d\t%d\t%d\t%d\t%d\n",j_feed,istart,iend,kstart,kend);


	} else if (use_shape == 2) {
		// dipole antenna
		for (k=kc-10; k < kc+10; k++) {
			gaz[ic][jc][k] = 0.0;
		}
		gaz[ic][jc][kc] = 1.0;
	} else if (use_shape == 3) {
		// dialectric sphere
		epsilon = 30.;
		sigma = 0.3;
		radius = 10.;
		epsilon_free = 1.;
		sigma_free = 0.;

		for (i=ia; i < ib; i++) {
			xdist = ic-i-0.5;
			for (j=ja; j < jb; j++) {
				ydist = jc-j;
				for (k=ka; k < kb; k++) {
					eps=epsilon_free;
					cond=sigma_free;
					zdist = kc-k;
					dist = sqrt(pow(xdist,2.) + pow(ydist,2.) + pow(zdist,2.));
					if (dist <= radius) {
						eps = epsilon;
						cond = sigma;
					}
					gax[i][j][k] = 1./(eps + (cond*dt/e0));
					gbx[i][j][k] = cond*dt/e0;
				}
			}
		}

		for (i=ia; i < ib; i++) {
			xdist = ic-i;
			for (j=ja; j < jb; j++) {
				ydist = jc-j-0.5;
				for (k=ka; k < kb; k++) {
					eps=epsilon_free;
					cond=sigma_free;
					zdist = kc-k;
					dist = sqrt(pow(xdist,2.) + pow(ydist,2.) + pow(zdist,2.));
					if (dist <= radius) {
						eps = epsilon;
						cond = sigma;
					}
					gay[i][j][k] = 1./(eps + (cond*dt/e0));
					gby[i][j][k] = cond*dt/e0;
				}
			}
		}

		for (i=ia; i < ib; i++) {
			xdist = ic-i;
			for (j=ja; j < jb; j++) {
				ydist = jc-j;
				for (k=ka; k < kb; k++) {
					eps=epsilon_free;
					cond=sigma_free;
					zdist = kc-k-0.5;
					dist = sqrt(pow(xdist,2.) + pow(ydist,2.) + pow(zdist,2.));
					if (dist <= radius) {
						eps = epsilon;
						cond = sigma;
					}
					gaz[i][j][k] = 1./(eps + (cond*dt/e0));
					gbz[i][j][k] = cond*dt/e0;
				}
			}
		}
	} else if (use_shape == 4) {

		kstart = 0;
		kend = 2;
		ktop = 2;
		istart = ia+9;
		iend = istart+6;
		i_ref = istart + (iend-istart)/2.;
		i_patch_st = ia+10;//ia+5;
		i_patch_end = i_patch_st + 31;
		j_patch_end = jb-5;
		j_patch_st = j_patch_end - 39;
		j_ref = j_patch_st - 30;
		k_ref = ktop-1;
		j_feed = ja;

		// patch antenna
		for (j=0; j < NY; j++) {
			for (i=0; i < NX; i++) {
				for (k=0; k <= ktop; k++) {
					gax[i][j][k] = 1./e_sub;
					gay[i][j][k] = 1./e_sub;
					gaz[i][j][k] = 1./e_sub;
				}
			}
		}
		for (j=1; j < NY-1; j++) {
			for (i=1; i < NX-1; i++) {
				gax[i][j][0] = 0.;
				gay[i][j][0] = 0.;
			}
		}

		for (i=istart; i <= iend; i++) {
			for (k=0; k <= ktop; k++) {
				feed[i][k] = 1.;
			}
		}

		printf("feed");
		for (j=1; j <= j_patch_st; j++) {
			for (i=istart; i <= iend-1; i++) {
				gax[i][j][ktop+1] = 0.;
				gay[i][j][ktop+1] = 0.;
				printf("%d\t%d\n",i,j);
			}
		}

		printf("patch");
		for (j=j_patch_st; j <= j_patch_end; j++) {
			for (i=ia+1; i <= ib-1; i++) {
				gax[i][j][ktop+1] = 0.;
				gay[i][j][ktop+1] = 0.;
				printf("%d\t%d\n",i,j);
			}
		}

	}

// ***********************************************
// ********** INITIALIZE TF/SF VARIABLES *********
// ***********************************************

	for (i=0; i < ia; i++) {
		for (j=0; j < NY; j++) {
			for (k=0; k < NZ; k++) {
				idxl[i][j][k] = 0.0;
				idxh[i][j][k] = 0.0;
				ihxl[i][j][k] = 0.0;
				ihxh[i][j][k] = 0.0;
			}
		}
	}

	for (i=0; i < NX; i++) {
		for (j=0; j < ja; j++) {
			for (k=0; k < NZ; k++) {
				idyl[i][j][k] = 0.0;
				idyh[i][j][k] = 0.0;
				ihyl[i][j][k] = 0.0;
				ihyh[i][j][k] = 0.0;
			}
		} 
	}

	for (i=0; i < NX; i++) {
		for (j=0; j < NY; j++) {
			for (k=0; k < ka; k++) {
				idzl[i][j][k] = 0.0;
				idzh[i][j][k] = 0.0;
				ihzl[i][j][k] = 0.0;
				ihzh[i][j][k] = 0.0;
			}
		}
	}

// ***********************************************
// ********** INITIALIZE PML PARAMETERS **********
// ***********************************************

	for (i=0; i < NX; i++) {
		gi1[i] = 0.0;
		gi2[i] = 1.0;
		gi3[i] = 1.0;
		fi1[i] = 0.0;
		fi2[i] = 1.0;
		fi3[i] = 1.0;
	}

	for (j=0; j < NY; j++) {
		gj1[j] = 0.0;
		gj2[j] = 1.0;
		gj3[j] = 1.0;
		fj1[j] = 0.0;
		fj2[j] = 1.0;
		fj3[j] = 1.0;
	}

	for (k=0; k < NZ; k++) {
		gk1[k] = 0.0;
		gk2[k] = 1.0;
		gk3[k] = 1.0;
		fk1[k] = 0.0;
		fk2[k] = 1.0;
		fk3[k] = 1.0;
	}

	// X
	for (i=0; i < NPML; i++) {
		xxn = (NPML-i)/NPML; // goes from 1 to 0
		xn = 0.33*pow(xxn,3.0);
		fi1[i] = xn;
		fi1[NX-i-1] = xn;
		gi2[i] = 1.0/(1.0+xn);
		gi2[NX-i-1] = 1.0/(1.0+xn);
		gi3[i] = (1.0-xn)/(1.0+xn);
		gi3[NX-i-1] = (1.0-xn)/(1.0+xn);

		xxn = (NPML-i-0.5)/NPML;
		xn = 0.33*pow(xxn,3.0);
		gi1[i] = xn;
		gi1[NX-i-2] = xn;
		fi2[i] = 1.0/(1.0+xn);
		fi2[NX-i-2] = 1.0/(1.0+xn);
		fi3[i] = (1.0-xn)/(1.0+xn);
		fi3[NX-i-2] = (1.0-xn)/(1.0+xn);
	}

	// Y
	for (j=0; j < NPML; j++) {
		xxn = (NPML-j)/NPML; // goes from 1 to 0
		xn = 0.33*pow(xxn,3.0);
		fj1[j] = xn;
		fj1[NY-j-1] = xn;
		gj2[j] = 1.0/(1.0+xn);
		gj2[NY-j-1] = 1.0/(1.0+xn);
		gj3[j] = (1.0-xn)/(1.0+xn);
		gj3[NY-j-1] = (1.0-xn)/(1.0+xn);

		xxn = (NPML-j-0.5)/NPML;
		xn = 0.33*pow(xxn,3.0);
		gj1[j] = xn;
		gj1[NY-j-2] = xn;
		fj2[j] = 1.0/(1.0+xn);
		fj2[NY-j-2] = 1.0/(1.0+xn);
		fj3[j] = (1.0-xn)/(1.0+xn);
		fj3[NY-j-2] = (1.0-xn)/(1.0+xn);
	}

	// Z
	for (k=0; k < NPML; k++) {
		xxn = (NPML-k)/NPML; // goes from 1 to 0
		xn = 0.33*pow(xxn,3.0);
		fk1[k] = xn;
		fk1[NZ-k-1] = xn;
		gk2[k] = 1.0/(1.0+xn);
		gk2[NZ-k-1] = 1.0/(1.0+xn);
		gk3[k] = (1.0-xn)/(1.0+xn);
		gk3[NZ-k-1] = (1.0-xn)/(1.0+xn);

		xxn = (NPML-k-0.5)/NPML;
		xn = 0.33*pow(xxn,3.0);
		gk1[k] = xn;
		gk1[NZ-k-2] = xn;
		fk2[k] = 1.0/(1.0+xn);
		fk2[NZ-k-2] = 1.0/(1.0+xn);
		fk3[k] = (1.0-xn)/(1.0+xn);
		fk3[NZ-k-2] = (1.0-xn)/(1.0+xn);
	}

// ***********************************************
// ************ OPEN DATA OUTPUT FILES ***********
// ***********************************************

	fp = fopen("data.dat","w");
	fp2 = fopen("ampl.dat","w");
	fprintf(fp,"%d\t%d\t%d\t%d\n ",NX,NY,NZ,NSTEPS);

// ***********************************************
// ****************** MAIN LOOP ******************
// ***********************************************

	for (n=1; n < NSTEPS; n++) {
		printf("step: %d\n",n);
		// PROPOGATE PULSE IN E-FIELD
		for (j=1; j < NY; j++) {
			ez_inc[j] = gj3[j]*ez_inc[j] + gj2[j]*(0.5*ra_y/e_sub)*(hx_inc[j-1] - hx_inc[j]);
			printf("%d\t%f\n",j,ez_inc[j]);
		}

		// FOURIER TRANSFORM INPUT WAVEFORM
		for (m=0; m < NFREQS; m++) {
			real_in[m] = real_in[m] + cos(arg[m]*T)*ez_inc[ja-1];
			imag_in[m] = imag_in[m] - sin(arg[m]*T)*ez_inc[ja-1];
		}

		// GENEREATE PULSE
		// pulse = 2.*sin(n/10); // HARMONIC
		// pulse = 2.*(1-2*pow(pi,2)*pow(0.5*n/f_peak-t0,2))*exp(-pow(pi,2)*pow(0.5*n/f_peak-t0,2.));
		pulse = 2.*exp(-0.5*pow((t0-n)/spread,2.0)); // GAUSSIAN PULSE
		// pulse = (1-exp(-0.5*pow((n)/spread,2.0)))*2.;//.*sin(n/10); // GAUSSIAN TURN-0N
		ez_inc[j_feed-2] = pulse;

// *********** DX ***********
		// SCATTERED FIELD
		for (i=1; i < ia; i++) {
			for (j=1; j<NY; j++) {
				for(k=1; k<NZ; k++) {
					curl_h = (ra_y*(hz[i][j][k] - hz[i][j-1][k]) - hy[i][j][k] + hy[i][j][k-1]);
					idxl[i][j][k] = idxl[i][j][k] + curl_h;
					dx[i][j][k] = gj3[j]*gk3[k]*dx[i][j][k] + gj2[j]*gk2[k]*0.5*(curl_h + gi1[i]*idxl[i][j][k]);
				}
			}
		}
		// TOTAL FIELD
		for (i=ia; i <= ib; i++) {
			for (j=1; j<NY; j++) {
				for(k=1; k<NZ; k++) {
					curl_h = (ra_y*(hz[i][j][k] - hz[i][j-1][k]) - hy[i][j][k] + hy[i][j][k-1]);
					dx[i][j][k] = gj3[j]*gk3[k]*dx[i][j][k] + gj2[j]*gk2[k]*0.5*curl_h;
				}
			}
		}
		// SCATTERED FIELD
		for (i=ib+1; i < NX; i++) {
			ixh = i - ib - 1;
			for (j=1; j<NY; j++) {
				for(k=1; k<NZ; k++) {		
					curl_h = (ra_y*(hz[i][j][k] - hz[i][j-1][k]) - hy[i][j][k] + hy[i][j][k-1]);
					idxh[ixh][j][k] = idxh[ixh][j][k] + curl_h;
					dx[i][j][k] = gj3[j]*gk3[k]*dx[i][j][k] + gj2[j]*gk2[k]*0.5*(curl_h + gi1[i]*idxh[ixh][j][k]);
				}
			}
		}

// *********** DY ***********
		// SCATTERED FIELD
		for (i=1; i < NX; i++) {
			for (j=1; j<ja; j++) {
				for(k=1; k<NZ; k++) {
					curl_h = (hx[i][j][k] - hx[i][j][k-1] - ra_x*(hz[i][j][k] - hz[i-1][j][k]));
					idyl[i][j][k] = idyl[i][j][k] + curl_h;
					dy[i][j][k] = gi3[i]*gk3[k]*dy[i][j][k] + gi2[i]*gk2[k]*0.5*(curl_h + gj1[j]*idyl[i][j][k]);
				}
			}
		}
		// TOTAL FIELD
		for (i=1; i < NX; i++) {
			for (j=ja; j<=jb; j++) {
				for(k=1; k<NZ; k++) {
					curl_h = (hx[i][j][k] - hx[i][j][k-1] - ra_x*(hz[i][j][k] - hz[i-1][j][k]));
					dy[i][j][k] = gi3[i]*gk3[k]*dy[i][j][k] + gi2[i]*gk2[k]*0.5*curl_h;
				}
			}
		}
		// SCATTERED FIELD
		for (i=1; i < NX; i++) {
			for (j=jb+1; j<NY; j++) {
				jyh = j - jb - 1;
				for(k=1; k<NZ; k++) {		
					curl_h = (hx[i][j][k] - hx[i][j][k-1] - ra_x*(hz[i][j][k] - hz[i-1][j][k]));
					idyh[i][jyh][k] = idyh[i][jyh][k] + curl_h;
					dy[i][j][k] = gi3[i]*gk3[k]*dy[i][j][k] + gi2[i]*gk2[k]*0.5*(curl_h + gj1[j]*idyh[i][jyh][k]);
				}
			}
		}

// *********** DZ ***********
		// SCATTERED FIELD
		for (i=1; i < NX; i++) {
			for (j=1; j<NY; j++) {
				for(k=0; k<ka; k++) {
					curl_h = (ra_x*(hy[i][j][k] - hy[i-1][j][k]) - ra_y*(hx[i][j][k] - hx[i][j-1][k]));
					idzl[i][j][k] = idzl[i][j][k] + curl_h;
					dz[i][j][k] = gi3[i]*gj3[j]*dz[i][j][k] + gi2[i]*gj2[j]*0.5*(curl_h + gk1[k]*idzl[i][j][k]);
				}
			}
		}
		// TOTAL FIELD
		for (i=1; i < NX; i++) {
			for (j=1; j<NY; j++) {
				for(k=ka; k<=kb; k++) {
					curl_h = (ra_x*(hy[i][j][k] - hy[i-1][j][k]) - ra_y*(hx[i][j][k] - hx[i][j-1][k]));
					dz[i][j][k] = gi3[i]*gj3[j]*dz[i][j][k] + gi2[i]*gj2[j]*0.5*curl_h;
				}
			}
		}
		// SCATTERED FIELD
		for (i=1; i < NX; i++) {
			for (j=1; j<NY; j++) {
				for(k=kb+1; k<NZ; k++) {
					kzh = k - kb - 1;
					curl_h = (ra_x*(hy[i][j][k] - hy[i-1][j][k]) - ra_y*(hx[i][j][k] - hx[i][j-1][k]));
					idzh[i][j][kzh] = idzh[i][j][kzh] + curl_h;
					dz[i][j][k] = gi3[i]*gj3[j]*dz[i][j][k] + gi2[i]*gj2[j]*0.5*(curl_h + gk1[k]*idzh[i][j][kzh]);
				}
			}
		}

// ******* INJECT SOURCE INTO D-FIELD *******
		for (i = istart; i <= iend; i++) {
			for (k=kstart; k <= kend; k++) {
				dz[i][j_feed][k] = dz[i][j_feed][k] + 0.5/e_sub*feed[i][k]*hx_inc[j_feed-1];
				dx[i][j_feed][k] = dx[i][j_feed][k] + 0.5/e_sub*feed[i][k]*hx_inc[j_feed-1];
			}
		}

// ******* CALCULATE E FIELD FROM D FIELD *******
		for (k=1; k < NZ-1; k++) {
			for (j=1; j < NY-1; j++) {
				for (i=1; i < NX-1; i++) {
					ex[i][j][k] = gax[i][j][k]*(dx[i][j][k] - ix[i][j][k]);
					ix[i][j][k] = ix[i][j][k] + gbx[i][j][k]*ex[i][j][k];
					ey[i][j][k] = gay[i][j][k]*(dy[i][j][k] - iy[i][j][k]);
					iy[i][j][k] = iy[i][j][k] + gby[i][j][k]*ey[i][j][k];
					ez[i][j][k] = gaz[i][j][k]*(dz[i][j][k] - iz[i][j][k]);
					iz[i][j][k] = iz[i][j][k] + gbz[i][j][k]*ez[i][j][k];
				}
			}
		}

// ******* PROPOGATE PULSE IN H-FIELD *******
		for (j=0; j < NY-1; j++) {
			hx_inc[j] = fj3[j]*hx_inc[j] + 0.5*fj2[j]*(ez_inc[j] - ez_inc[j+1]);
		}

// *********** HX ***********
		// SCATTERED FIELD
		for (i=0; i < ia; i++) {
			for (j=0; j<NY-1; j++) {
				for(k=0; k<NY-1; k++) {
					curl_e = (ey[i][j][k+1] - ey[i][j][k] - ra_y*(ez[i][j+1][k] - ez[i][j][k]));
					ihxl[i][j][k] = ihxl[i][j][k] + curl_e;
					hx[i][j][k] = fj3[j]*fk3[k]*hx[i][j][k] + fj2[j]*fk2[k]*0.5*(curl_e + fi1[i]*ihxl[i][j][k]);
				}
			}
		}
		// TOTAL FIELD
		for (i=ia; i <= ib; i++) {
			for (j=0; j<NY-1; j++) {
				for(k=0; k<NZ-1; k++) {
					curl_e = (ey[i][j][k+1] - ey[i][j][k] - ra_y*(ez[i][j+1][k] - ez[i][j][k]));
					hx[i][j][k] = fj3[j]*fk3[k]*hx[i][j][k] + fj2[j]*fk2[k]*0.5*curl_e;
				}
			}
		}
		// SCATTERED FIELD
		for (i=ib+1; i < NX; i++) {
			ixh = i - ib - 1;
			for (j=0; j<NY-1; j++) {
				for(k=0; k<NZ-1; k++) {		
					curl_e = (ey[i][j][k+1] - ey[i][j][k] - ra_y*(ez[i][j+1][k] - ez[i][j][k]));
					ihxh[ixh][j][k] = ihxh[ixh][j][k] + curl_e;
					hx[i][j][k] = fj3[j]*fk3[k]*hx[i][j][k] + fj2[j]*fk2[k]*0.5*(curl_e + fi1[i]*ihxh[ixh][j][k]);
				}
			}
		}

// ******* INJECT SOURCE INTO HX-FIELD *******
		for (i=istart; i <= iend; i++) {
			for (k=kstart; k <= kend; k++) {
				hx[i][j_feed-1][k] = hx[i][j_feed-1][k] + 0.5/e_sub*feed[i][k]*ez_inc[j_feed];
				hy[i][j_feed-1][k] = hy[i][j_feed-1][k] + 0.5/e_sub*feed[i][k]*ez_inc[j_feed];
			}
		}

// *********** HY ***********
		// SCATTERED FIELD
		for (i=0; i < NX-1; i++) {
			for (j=0; j < ja; j++) {
				for (k=0; k < NZ-1; k++) {
					curl_e = (ra_x*(ez[i+1][j][k] - ez[i][j][k]) - ex[i][j][k+1] + ex[i][j][k]);
					hy[i][j][k] = fi3[i]*fk3[k]*hy[i][j][k] + fi2[i]*fk3[k]*0.5*(curl_e + fj1[j]*ihyl[i][j][k]);
				}
			}
		}
		// TOTAL FIELD
		for (i=0; i < NX-1; i++) {
			for (j=ja; j<=jb; j++) {
				for(k=0; k<NZ-1; k++) {
					curl_e = (ra_x*(ez[i+1][j][k] - ez[i][j][k]) - ex[i][j][k+1] + ex[i][j][k]);
					hy[i][j][k] = fi3[i]*fk3[k]*hy[i][j][k] + fi2[i]*fk2[k]*0.5*curl_e;
				}
			}
		}
		// SCATTERED FIELD
		for (i=0; i < NX-1; i++) {
			for (j=jb+1; j<NY; j++) {
				jyh = j - jb - 1;
				for(k=0; k<NZ-1; k++) {		
					curl_e = (ra_x*(ez[i+1][j][k] - ez[i][j][k]) - ex[i][j][k+1] + ex[i][j][k]);
					ihyh[i][jyh][k] = ihyh[i][jyh][k] + curl_e;
					hy[i][j][k] = fi3[i]*fk3[k]*hy[i][j][k] + fi2[i]*fk2[k]*0.5*(curl_e + fj1[j]*ihyh[i][jyh][k]);
				}
			}
		}

// *********** HZ ***********
		// SCATTERED FIELD
		for (i=0; i < NX-1; i++) {
			for (j=0; j<NY-1; j++) {
				for(k=0; k<ka; k++) {
					curl_e = (ra_y*(ex[i][j+1][k] - ex[i][j][k]) - ra_x*(ey[i+1][j][k] - ey[i][j][k]));
					ihzl[i][j][k] = ihzl[i][j][k] + curl_e;
					hz[i][j][k] = fi3[i]*fj3[j]*hz[i][j][k] + fi2[i]*fj2[j]*0.5*(curl_e + fk1[k]*ihzl[i][j][k]);
				}
			}
		}
		// TOTAL FIELD
		for (i=0; i < NX-1; i++) {
			for (j=0; j<NY-1; j++) {
				for(k=ka; k<=kb; k++) {
					curl_e = (ra_y*(ex[i][j+1][k] - ex[i][j][k]) - ra_x*(ey[i+1][j][k] - ey[i][j][k]));
					hz[i][j][k] = fi3[i]*fj3[j]*hz[i][j][k] + fi2[i]*fj2[j]*0.5*curl_e;
				}
			}
		}
		// SCATTERED FIELD
		for (i=0; i < NX-1; i++) {
			for (j=0; j<NY-1; j++) {
				for(k=kb+1; k<NZ; k++) {
					kzh = k - kb - 1;
					curl_e = (ra_y*(ex[i][j+1][k] - ex[i][j][k]) - ra_x*(ey[i+1][j][k] - ey[i][j][k]));
					ihzh[i][j][kzh] = ihzh[i][j][kzh] + curl_e;
					hz[i][j][k] = fi3[i]*fj3[j]*hz[i][j][k] + fi2[i]*fj2[j]*0.5*(curl_e + fk1[k]*ihzh[i][j][kzh]);
				}
			}
		}

// *****************************
// ***** WRITE OUT TO FILE *****
// *****************************
		for (k=0; k < NZ; k++) {
			for ( j=0; j < NY; j++) {
				for ( i=0; i < NX; i++) {
					fprintf(fp,"%7.4f\n",ez[i][j][k]+0.3*(1-gax[i][j][k]));//ez[i][j][k]+0.2*(1-gax[i][j][k])
				}
			}
		}

		// FOURIER TRANSFORM OUTPUT WAVEFORM
		for (j=0; j < NY; j++) {
			for (i=0; i < NX; i++) {
				for (m=0; m < NFREQS; m++) {
					real_pt[m][i][j] = real_pt[m][i][j] + cos(arg[m]*T)*ez[i][j][kc];
					imag_pt[m][i][j] = imag_pt[m][i][j] - sin(arg[m]*T)*ez[i][j][kc]; // + or - sin?
				}
			}
		}

		for (m=0; m < NFREQS; m++) {
			ampl_in[m] = sqrt(pow(real_in[m],2.) + pow(imag_in[m],2.));
			phase_in[m] = atan2(imag_in[m],real_in[m]);
		}
		
	}
	for (m=0; m < NFREQS; m++) {	
		if (m == 2)	{		//fp = fopen("ampl1","w");
			// else if (m == 1)	fp = fopen("ampl2")	
			for (j=ja; j <= jb; j++) {
				if (gaz[ic][j][kc] < 1.0) {
					ampl[ic][j] = (1./ampl_in[m])*sqrt(pow(real_pt[m][ic][j],2.) + pow(imag_pt[m][ic][j],2.)); // parens?
					// fprintf(fp2,"%d\t%9.4f\n",j,ampl[ic][j]);
					fprintf(fp2,"%9.4f\n",ampl[ic][j]);
				}
			}
		}
	}
	fclose(fp2);
	fclose(fp);

}