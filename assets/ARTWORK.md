# Artwork and animation

Original: Hans Holbein the Younger, *Jean de Dinteville and Georges de Selve ('The Ambassadors')*, 1533. Oil on oak, 207 × 209.5 cm. National Gallery, London, NG1314.

[Collection record and painting reference](https://www.nationalgallery.org.uk/paintings/hans-holbein-the-younger-the-ambassadors).

`ambassadors-still.png` is a new AI-generated adaptation, made using the built-in Image Generation tool with the original painting as a visual reference. It is not an unaltered reproduction or a portrait of Sadra. The laptop and notebook connect the painting's measuring instruments with his work on clinical judgment and his writing.

`ambassadors.gif` is an 8-second, 660 × 440, infinitely looping camera animation of that adaptation. It uses a restrained 2.5% push-in and return. The characters are still; this is not generated character motion. The still image is available from the profile for readers who prefer no animation.

Rebuild with Pillow installed: `python3 scripts/animate.py`.

## Generation prompt

Use case: style-transfer. Asset: a refined GitHub profile hero illustration, to be animated later as a quiet looping GIF. Reference image: Hans Holbein the Younger, The Ambassadors (1533), compositional and painting reference. Create a recognizable, respectful contemporary adaptation for Sadra Ali, a writer and product builder working on machine judgment in health and clinical triage. Preserve both original historical sitters, their faces, richly painted clothing, green damask curtain, patterned carpet, astronomical instruments, lute, and especially the elongated anamorphic skull in the foreground. Do not depict a new portrait of Sadra. The subtle contemporary intervention: place a small open dark laptop on the lower shelf among the books and instruments, its dim warm ivory screen showing a very simple thin-line clinical decision tree with small amber nodes, no readable text. A slim handwritten notebook next to it connects to his writing. These should feel painted in the same Northern Renaissance oil technique, integrated with the objects, not pasted or neon. Composition: landscape 1536x1024, extend the environment at the sides to fit both figures entirely from hats to feet and retain the entire distorted skull; never squash or crop the subjects. Gallery-quality meticulous oil-on-oak texture, deep muted forest greens, warm brass, burgundy, creamy highlights. Restrained, contemplative, intellectual. No typography, no labels, no logos, no border, no modern robot, no science-fiction UI. The image should work as a calm editorial banner with no extra graphics. Output one image.
