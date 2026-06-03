#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#define NX 60
#define NY 60

main()
{
	float ga[NX][NY], dz[NX][NY], ez[NX][NY], hx[NX][NY], hy[NX][NY];
	int l,n,i,j,ic,jc,nsteps;
	float ddx,dt,T,epsz,pi,epsilon,sigma,eaf;
	float t0, spread, pulse;
	FILE *fp, *fopen();

	ic = NX/2;
	jc = NX/2;
	ddx = 0.01;
	dt = ddx/6e8;
	epsz = 8.8e-12;
	pi = 3.14159;

	for (j=0; j < NY; j++) {
		printf( "%2d 	",j);
		for (i=0; i < NX; i++) {
			dz[i][j] = 0.;
			ez[i][j] = 0.;
			hx[i][j] = 0.;
			hy[i][j] = 0.;
			ga[i][j] = 1.0;
			printf("%5.2f",ga[i][j]);
		}
		printf("\n");
	}

	t0 = 20.0;
	spread = 6.0;
	T = 0;
	nsteps = 100;

	fp = fopen("2d_data.dat","w");
	// while (nsteps > 0) {
		// printf("nsteps --> ");
		// scanf("%d", &nsteps);
		// printf("%d \n", nsteps);

		for ( n=1; n <= nsteps ; n++) {
			T = T + 1;

			/* --- MAIN FDTD LOOP --- */
			for ( j=1; j < NY; j++) {
				for ( i=1; i < NX; i++) {
					dz[i][j] = dz[i][j] + 0.5*(hy[i][j] - hy[i-1][j] - hx[i][j] + hx[i][j-1]);
				}
			}

			// pulse = exp(-0.5*(pow((t0-T)/spread,2.0)));
			// dz[ic-20][jc-20] = pulse;
			// dz[ic+30][jc+30] = pulse;

			// if (n == 1) {
			// 	dz[ic][jc] = 1.0;
			// }


			pulse = exp(-0.5*(pow((t0-T)/spread,2.0)));
			for ( j = jc-20; j < jc+20; j++) {
				// dz[1][j] = pulse;
				dz[2][j] = pulse/20.;
			}

			/* --- boundary conditions --- */
			for ( j=1; j < NY; j++) {
				dz[0][j] = 0.0;
				dz[1][j] = 0.0;
				dz[NX][j] = 0.0;
				dz[NX-1][j] = 0.0;
			}
			for ( i=1; i < NY; i++) {
				dz[i][0] = 0.0;
				dz[i][1] = 0.0;
				dz[i][NY] = 0.0;
				dz[i][NY-1] = 0.0;
			}

			for ( j=1; j < NY; j++) {
				for ( i=1; i < NX; i++) {
					ez[i][j] = ga[i][j]*dz[i][j];
				}
			}

			for ( j=0; j < NY-1; j++) {
				for ( i=0; i < NX-1; i++) {
					hx[i][j] = hx[i][j] + 0.5*(ez[i][j] - ez[i][j+1]);
 				}
			}

			for ( j=0; j < NY-1; j++) {
				for ( i=0; i < NX-1; i++) {
					hy[i][j] = hy[i][j] + 0.5*(ez[i+1][j] - ez[i][j]);
				}
			}
			/* --- MAIN FDTD LOOP --- */

			// for ( j=1; j < jc; j++) {
			// 	printf( "%2d 	",j);
			// 	for ( i=1; i < ic; i++) {
			// 		printf("%5.2f",ez[2*i][2*j]);
			// 	}
			// 	printf("\n");
			// }
			// printf("T = %5.0f \n", T);

			
			for ( j=0; j < NY; j++) {
				for ( i=0; i < NX; i++) {
					fprintf(fp,"%6.3f ",ez[i][j]);
				}
				fprintf(fp, " \n");
			}
			fprintf(fp, "# N = %d \n", n);	
		}
	// }
		fclose(fp);
}