% Load the image
img = imread('your_image.jpg'); % Replace 'your_image.jpg' with the file path to your image

% Convert the image to grayscale
grayImg = rgb2gray(img);

% Use thresholding to separate the foreground from the background
threshold = graythresh(grayImg); % Compute an automatic threshold
binaryImg = imbinarize(grayImg, threshold);

% Clean up the binary image (optional)
binaryImg = bwareaopen(binaryImg, 100); % Remove small objects

% Create a mask for the foreground
foregroundMask = imcomplement(binaryImg);

% Apply the mask to the original image to remove the background
resultImg = img;
resultImg(repmat(foregroundMask, [1, 1, 3])) = 255; % Set background to white

% Display the resulting image
imshow(resultImg);
