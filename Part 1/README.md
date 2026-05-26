# Part 1

This is the beginning of the Evolutionary Computation course, which is divided into different implementations and algorithm structures, starting with optimization of equations using Python and preparation of the GPU environment. In this README, I'll present the problems of each section, and their solutions will be in this Part 1 folder.

## T1 - Analysis of a CUDA program

A digital image can be represented with a 1-dimensional or 2-dimensional array of different intensity pixels:

$$
img=[p_0,p_1,p_2,...,p_n]
$$

where every element $p_i$ corresponds to the intensity pixel value.

### Transformation

The goal here is to apply an independent transformation to each pixel to generate a new output image:

$$
out[i]=255-img[i]
$$

This operation produces a **negative image**, which will invert the intensities of the pixels (high values will be turned into low values and vice versa).

From a computational view, this problem is an example of **data massive parallelism**, because:

* Every element of the array will be processed in an independent way
* Dependency does NOT exist between pixels
* It's possible to assign a *thread* per element

With these parameters, the ideal case will be to implement it using GPU architectures with models like CUDA.





