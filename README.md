<h1>Automatic Picking of Microtubule Proteins and Microtubule Doublet Proteins in Cilia and Flagella</h1>
<p>This is my repository for the 2020 SURA research project @ Khanh Huy Bui Lab, Department of Anatomy and Cell Biology at McGill University</p>
<h2> Implemented Tools </h2>
<ol>
  <li>Integration of the Topaz Machine Learning Program by @Tbepler</li>
  <li>A polynomial fitting tool for discrete microtubule coordinates</li>
  <li>File parsers and writers for different formats of coordinate files supported by different softwares</li>
  <li>(Upcoming) A complete workflow and encapsulated program for automatic cryo-em picking of microtubules and doublet microtubules. </li>
  <li>(Upcoming) A GUI for automatic picking of microtubule micrographs</li>

</ol>

<h2>Prerequisites
</h2>

<ol>
  <li>Download Numpy, Matplotlib, and Scikit-Learn</li>
  <span style="margin-left: 40px"> <i>pip install numpy matplotlib scikit-learn</i></span>
  <li>Download topaz: https://github.com/tbepler/topaz</li>
  <li>Clone this repository</li>
</ol>

<h3>Instructions to perform particle picking</h3>
<p>to be added</p>

<b>RANSACFit</b>

RANSAC fit, also known as Random Sample Consensus, is an iterative method to estimate parameters of a mathematical model from a set of observed data that contains outliers, when e outliers are accorded no influence on the values of the estimates. (https://en.wikipedia.org/wiki/Random_sample_consensus#:~:text=Random%20sample%20consensus%20(RANSAC)%20is,the%20values%20of%20the%20estimates.)

This python script contains functions needed to perform RANSAC polynomial interpolation on scatter plot data. As well as the functions to mark the interpolated line evenly spaced along its arclength. These functions are intended for the process of Cryo-EM, where coordinate interpolations are to be made on picked coordinates along a filament.

The input X and Y coordiantes are to be provided in CSV format or in Numpy format. Test data sets can be found in test_data, it contains about 9000 csv files each representing the picked coordinates of a biological filament molecule. Using the functions provided in the RANSACFIT script, one can generate the interpolation of these picked coordinates, as well as the coordinates of evenly spaced marks along the interpolated line for the purpose of biological helical processing.

<citations>Citations</citations>
<ul><li>Tristan Bepler. 2019. Topaz. https://github.com/tbepler/topaz (2020)</li><ul>

