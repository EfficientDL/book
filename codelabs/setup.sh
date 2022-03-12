# Might not run well on OSX. I think perhaps wget is spawned in some other
# process?
#
# Install the fonts.
mkdir fonts/

# Download the fonts we need.
wget -qO Noto_Sans.zip https://drive.google.com/uc?id=1-0tqK8qCFRVqsRZag4YYJmy2ZnPOD5VD&export=download 
unzip -qo Noto_Sans.zip -d fonts/Noto_Sans
wget -qO Roboto.zip https://drive.google.com/uc?id=1Xo2EUtHc5CIAo3l5V1FbtRopbV7_u-Cu&export=download
unzip -qo Roboto.zip -d fonts/Roboto
wget -qO Poppins.zip https://drive.google.com/uc?id=18Flk0fW_8RBNmKyDJEnMA43GjFjxp-i0&export=download
unzip -qo Poppins.zip -d fonts/Poppins

# wget + unzip is a little weird on OSX. You might have to comment the following
# line for this script to work on OSX.
#
# Works fine on Colab
# rm Noto_Sans.zip Roboto.zip Poppins.zip