def function[ret] = cac(value1, value2, value3, value4, value5, value6):
    aa(1, 1) = value6 - value5
    aa(2, 1) = value6 - value4
    aa(3, 1) = value6 - value3
    aa(4, 1) = value6 - value2
    aa(5, 1) = value6 - value1
    aa(6, 1) = value5 - value4
    aa(7, 1) = value5 - value3
    aa(8, 1) = value5 - value2
    aa(9, 1) = value5 - value1
    aa(10, 1) = value4 - value3
    aa(11, 1) = value4 - value2
    aa(12, 1) = value4 - value1
    aa(13, 1) = value3 - value2
    aa(14, 1) = value3 - value1
    aa(15, 1) = value2 - value1

    tmp = zeros(15, 1)

    for ii=1:15
        if aa(ii, 1) == aa(1, 1)
            tmp(1, 1) = tmp(1, 1) + 1

        if aa(ii, 1) == aa(2, 1)
            tmp(2, 1) = tmp(2, 1) + 1

        if aa(ii, 1) == aa(3, 1)
            tmp(3, 1) = tmp(3, 1) + 1

        if aa(ii, 1) == aa(4, 1)
            tmp(4, 1) = tmp(4, 1) + 1

        if aa(ii, 1) == aa(5, 1)
            tmp(5, 1) = tmp(5, 1) + 1

        if aa(ii, 1) == aa(6, 1)
            tmp(6, 1) = tmp(6, 1) + 1

        if aa(ii, 1) == aa(7, 1)
            tmp(7, 1) = tmp(7, 1) + 1

        if aa(ii, 1) == aa(8, 1)
            tmp(8, 1) = tmp(8, 1) + 1

        if aa(ii, 1) == aa(9, 1)
            tmp(9, 1) = tmp(9, 1) + 1

        if aa(ii, 1) == aa(10, 1);
            tmp(10, 1) = tmp(10, 1) + 1;

        if aa(ii, 1) == aa(11, 1);
            tmp(11, 1) = tmp(11, 1) + 1;

        if aa(ii, 1) == aa(12, 1);
            tmp(12, 1) = tmp(12, 1) + 1;

        if aa(ii, 1) == aa(13, 1);
            tmp(13, 1) = tmp(13, 1) + 1;

        if aa(ii, 1) == aa(14, 1);
            tmp(14, 1) = tmp(14, 1) + 1;

        if aa(ii, 1) == aa(15, 1);
            tmp(15, 1) = tmp(15, 1) + 1;

    tmp1 = 0;
    tmp2 = 0;
    tmp3 = 0;
    tmp4 = 0;
    tmp5 = 0;
    tmp6 = 0;

    for ii=1:15
        if tmp(ii, 1) == 1
            tmp1 = tmp1 + 1;

        if tmp(ii, 1) == 2
            tmp2 = tmp2 + 1;

        if tmp(ii, 1) == 3
            tmp3 = tmp3 + 1;

        if tmp(ii, 1) == 4
            tmp4 = tmp4 + 1;

        if tmp(ii, 1) == 5
            tmp5 = tmp5 + 1;

        if tmp(ii, 1) == 6
            tmp6 = tmp6 + 1;


ret = tmp1 + tmp2 / 2 + tmp3 / 3 + tmp4 / 4 + tmp5 / 5 + tmp6 / 6 - 5;

cac()