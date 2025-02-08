# IVP Midsem Notes

## Imaging System

- H/W + S/W to capture, process, and display images
- array of sensors to convert light signals to electrical signals
- major subsystems
    - optical sys - lens + paerture + shutter
    - image sensor - converts optical img to electrical signal
    - DSP sys - processes captured signal for enhancement, compression, and storage
        - functions
            - image enhancement - noise reduction, contrast adjustment, sharpening, etc.
            - compression - JPEG, PNG, etc.
                - lossy - by removal of some data; JPEG
                - lossless - by removal of unnecessary metasat wihtout any discernible loss in quality; PNG
- sampling theorem
- sampling
    - process of convering a continuous time signal to a discrete tiem signal by measuring its amplitude at regular intervals
    - Fourier Analysis is performed to find the component sin waves of a signal
    - sampling theorem - for a band-limited signal of max freq x Hz, atleast 2x samples must be taken to rep the signal

> band-limited samples are those that can be completely reconstructed from its samples

- quantization
    - process of mapping continous amplitude/intensity vals into discrete levels
    - crucial step in img compression
    - number of levels available for quantization depends of bith depth n = 2<sup>n</sup>
    - more levels reduce quanitsation error
    - type
        - uniform - equal-sized intervals
        - non-uniform - unequal-sized intervals
    - types of resolution
        - spetial resolution - dependent on number of sensors
        - intensity resolution - dependent of accurate representation of intensity variations
    ![alt text](<Screenshot from 2025-02-06 23-24-44.png>)

## Gaussian Distribution
- PDF
![alt text](<Screenshot from 2025-02-06 23-35-04.png>)
- higher std. dev. makes a wider curve and lower std. dev. makes a narrower curve
- CDF
![alt text](<Screenshot from 2025-02-06 23-52-15.png>)
![alt text](<Screenshot from 2025-02-06 23-52-21.png>)
- normalized distribution; mean = 0, std. dev. = 1
![alt text](<Screenshot from 2025-02-07 00-09-45.png>)

> standard deviation represents the amount of variation of a variable about its mean

## Image Filtering

- types
    - point processing
        - operates on each pixel independently
        - brightness, contrast, etc.
        - Gamma correction
            - correction applied to a pixel based on the characteristics of the display
            - non-linear operation used to adjust brightness and contrast of an image
            - mimics human vision in the sense that eyes are more sensitive to darker areas than bright ones
            ![alt text](<Screenshot from 2025-02-07 08-45-16.png>)
    - neighbourhood processing
        - modifies pixel based on surrounding pixels
        - smoothing, sharpening, blurring, etc.
        - linear(weighted sum) shift invariant(uniform application of filter across image) image filtering
            - each pixel is replaced by a linear combination of its neighboruing pixels
- filtering processes
    - convolution
        - flips kernel before applying it on the image
        - for a 2D kernel, it is transposed and applied on the image
        ![alt text](<Screenshot from 2025-02-07 08-58-08.png>)
    - correlation
        - doesn't flip kernel before application
        ![alt text](<Screenshot from 2025-02-07 08-58-41.png>)
    ![alt text](<WhatsApp Image 2025-02-07 at 14.10.11.jpeg>)
- box/mean filter
    - for uniform filtering
    - properties
        - blurs image by averaging intensities
        - reduces noise
    - for smoothing and reducing noise before edge detection
    ![alt text](<Screenshot from 2025-02-07 09-04-33.png>)
- Gaussian filter
     - theoretically infinite but we bound it to the max size of the kernel
     - we usually bound it as 2 - (3 * sigma)
- for smooth filtering
    - properties
        - smooths noise while preserving edges
        - more natural blurring effect
    - used for denoising images
    ![alt text](<Screenshot from 2025-02-07 09-04-38.png>)
    ![alt text](<Screenshot from 2025-02-07 09-04-43.png>)
- misc
    - zero padding is performed at the edges of images to apply filters; no. of rows/columns to be zero-padded on either side of the input image is given by no. of rows/columns in the kernel - 1
    ![alt text](<Screenshot from 2025-02-07 10-32-20.png>) 
    - separable filters
        - filters that can be represented as the product of a row and a column 
        - for an M * M img and N * N kernel
            - non-separable - M<sup>2</sup>N<sup>2</sup> convolutions
            - separable - 2M<sup>2</sup>N convolutions
        - separable filters reduce the number of computations
    - noise
        - random variations in pixel intensity
        - obscures img details
    - rank of a matrix - no. of independent rows/columns

https://16385.courses.cs.cmu.edu/fall2020/lecture/filtering/slide_001