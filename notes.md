# Room Scanner top-level class
 * handles GUI stuff (tkinter)
  * (*should it delegate GUI stuff to an inner object?*)
  * There should only be one class handling user-interaction
 * instantiates necessary objects:
  * Image Bin / image receiving class
  * Stitcher class
  * Image Analyser class (coordinate systems)
  * Plotter class
  * Space Planning class (interacts with Plotter)

## Image Bin
  Interacts with UI, takes in images/folder of images,
  loads them to memory as needed

## Stitcher
  Interacts with Image Bin to go from several photos to
  one 360-degree image.

## Image Analyser
  Gets panorama image from Image Bin, and picks out
  key elements (corners of the room, doorways, etc.).

  Has mapper functions to go from pixel coordinates
  of the panorama to angular coordinates in the
  room, from the 3D Origin (the point a user rotates
    about while taking photos)

## Plotter
  Uses the panoramic image, and the mappers from
  Image Analyser, to plot the room into a 2D top-down
  diagram. Diagram contains doorways, corners, and
  relative dimensions.

  *is the problem of measuring dimensions part
  of the Plotter or part of the Image Analyser?*

## Space Planning
  Contains inventories, places objects on top of Plot.
