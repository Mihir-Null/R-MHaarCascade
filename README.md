Haar cascade classifier pycharm project file for R@M testudog
current cascades have all been trained on positive images taken on phone and negatives sampled from the original haar paper
Current performance isn't great as the positive and negative images were all taken on different cameras from the one the final model was trained on, 
only 50 positive images turned out to be useful as well and approximately ~200 are needed at minimum

**Adding positive and negative images and training a new cascade:**
Positive and negative images can be found in the positives and negatives folders
the text files pos.txt and neg.txt specify the actual positives and negatives fed into the classifier with the additional numbers 
in the pos.txt specifying the number and locations of objects in the image

A new pos.txt can be created by cding into opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=(positive folder path) 
and using the tool to highlight the object(s) to be trained on in all positive images
Then create the vector of positives using:
opencv_createsamples.exe -info pos.txt -w (detection window width) -h (detection window height)

A new cascade can be generated using opencv_traincascade in the opencv bin and running opencv_traincascade.exe -data (folder to store cascade, usually cascade/) -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos (number of objects, use less than the actual number of samples) -numNeg (number of negative images, use any number as the trainer samples the negatives for actual negatives, try between 1/2 number of positives and 2x number of positives) -numStages (recommend ~10-14)
