# CAM Analysis

In this section, I look at what parts of each image the model focuses on when making predictions.  
The colored heatmaps show which areas the model thinks are important. Red means high focus.

---

## dog_pos — Predicted: pug

The heatmap is mainly on the dog’s face, especially around the eyes and nose.  
This makes sense because these features help identify a pug.  
The prediction is correct.

---

## dog_neg — Predicted: king_penguin

The model focuses on the penguin’s body and head.  
Since there is no dog in the image, the model guesses another animal it recognizes.  
The wrong prediction is expected.

---

## cat_pos — Predicted: Egyptian_cat

The heatmap highlights the cat’s face and ears.  
These are typical features for cats, so the model makes a correct prediction.

---

## cat_neg — Predicted: hamster

The model focuses on the hamster’s face and small round body.  
There is no cat in the image, so the model guesses a small animal instead.  
The wrong prediction is reasonable.

---

## car_pos — Predicted: minivan

The heatmap is on the front of the car, especially the shape and lights.  
These are important features for recognizing vehicles.  
The prediction is wrong, but the model still focuses on relevant parts of the image.

---

## car_neg — Predicted: snorkel

The model highlights random areas of the beach and water.  
Since there is no car in the image, the model guesses something unrelated.  
This shows that the model becomes unsure when it cannot find car-like shapes.

---

## Conclusion

The CAM images help explain why the model is right or wrong.  
When the prediction is correct, the model focuses on the important parts of the object.  
When the prediction is wrong, the heatmap is on irrelevant areas.  
CAM is useful for understanding how the model “looks” at images.
