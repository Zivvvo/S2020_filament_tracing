<b>RANSACFit</b>

RANSAC fit, also known as Random Sample Consensus, is an iterative method to estimate parameters of a mathematical model from a set of observed data that contains outliers, when e outliers are accorded no influence on the values of the estimates. (https://en.wikipedia.org/wiki/Random_sample_consensus#:~:text=Random%20sample%20consensus%20(RANSAC)%20is,the%20values%20of%20the%20estimates.)

This python script contains functions needed to perform RANSAC polynomial interpolation on scatter plot data. As well as the functions to mark the interpolated line evenly spaced along its arclength. These functions are intended for the process of Cryo-EM, where coordinate interpolations are to be made on picked coordinates along a filament.

The input coordiantes are to be provided in CSV format. Test data sets can be found in test_data, it contains about 9000 csv files each representing the picked coordinates of a biological filament molecule. Using the functions provided in the RANSACFIT script, one can generate the interpolation of these picked coordinates, as well as the coordinates of evenly spaced marks along the interpolated line for the purpose of biological helical processing.

