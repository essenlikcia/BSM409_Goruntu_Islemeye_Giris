import sys
import cv2 as cv

def main(argv):
    # vars
    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "laplace demonstration"

    imageName = argv[0] if len(argv) > 0 else "moon.jpg"
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)

    if src is None:
        print("error")
        return 0

    # remove noise by blurring image with gaussian filter
    src = cv.GaussianBlur(src, (3, 3), 0)

    # convert image to grayscale
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # create window
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # laplace func
    dst = cv.Laplacian(src_gray, ddepth, ksize = kernel_size)

    # convert back to uint8
    abs_dst = cv.convertScaleAbs(dst)

    # display
    cv.imshow(window_name, abs_dst)
    cv.waitKey()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])