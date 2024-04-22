import SimpleITK as sitk
import numpy as np

image = sitk.ReadImage("data/raw_data/test_image.nrrd")
roi_image = sitk.ReadImage("data/raw_data/test_image_rois.nrrd")

array = sitk.GetArrayFromImage(image)
roi_array = sitk.GetArrayFromImage(roi_image)

np.save("data/processed_data/image_array.npy", array)
np.save("data/processed_data/rois_array.npy", roi_array)