Planet order
============

This dasboard application based on the `sepal-ui <https://sepal-ui.readthedocs.io/en/latest/>`_ framework, provide the user with a friendly interface to explore and download Planet Labs images.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/demo.gif
    :group: planet-order
    
.. warning::

    in order to start this module, you need to have register on the planet NICFI contract (`Register NICFI PlanetLab <https://docs.sepal.io/en/latest/setup/register.html#sign-up-for-planet-lab-data>`_) and connect your GEE account to SEPAL (`connect GEE to SEPAL <https://docs.sepal.io/en/latest/setup/gee.html#connection-between-gee-and-sepal>`_).
    
In the landing page of our module at the bottom of the rigth drawer, You'll find 3 buttons: 

-   The :code source: will open in a new tab the GitHub repository that is used to create this module. our code is open-source and distributed under the MIT License.
    
    .. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/code_source.png
        :width: 17%
        :group: planet-order

-   The :wiki: button will lead you to this page

    .. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/wiki.png
        :width: 17%
        :group: planet-order
        
-   The :bug report: will open in a new tab the isse tracker of our GitHub repository. You can write here if you experience bugs or if you have any feature request. Our maintainer will answer as fast as possible.

    .. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/bug_report.png
        :width: 17%
        :group: planet-order
    
Select an AOI
-------------

The application use the same AOI selector that you will find in lots of other application in SEPAL. It is using GEE to provide several options of data selection. 

In this application multiple selection methods are available by selecting options in the first dropdown menu:

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/method.png
    :width: 50%
    :group: planet-order
    
Administrative
^^^^^^^^^^^^^^

Using one of the administrative options (:code:`country`, :code:`first administrative layer` or :code:`second administrative layer`), It will retreive information from the FAO GAUL 2015 GEE dataset. This isnformation will be used along the app to define your AOI

Customs
^^^^^^^

Several options are availalbe to select custom AOI including : `gee assets`, `draw a shape`, `upload a shapefile`.

.. tip:: 

    :code:`upload a shapelfile` will upload a shapefile that already exist in your SEPAL folder to GEE.
    If you want to us a shapefile that comes from your computer you need to upload it to SEPAL first using the `Vector file manager <https://docs.sepal.io/en/latest/modules/dwn/import_to_gee.html>`_.

Load PLanet Lab information
---------------------------

To use the module you'll need the Planet Lab API key associated to you Planet lab account

.. note::

    If you're not yet register to Planet please follow our `documentation <https://docs.sepal.io/en/latest/setup/register.html#sign-up-for-planet-lab-data>`_
    
Move to the :code:`retreive images` page by clicking on the button in the drawer. 
There, you'll find an empty map and several field that you need to fill.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/retreive_landing.png
    :group: planet-order
    
Provide your API key and click on :code:`check API key`. The tool will verify the validity of your API key. If this step is successful the list of all the mosaics available through your Planet account will be displayed in the planet mosaic dropdown and the mosaic selector system will be unabled.

.. note::
    
    If you want to check your API key click on the eye at the end of the password field, the password will be displayed. 
    
.. danger::

    Don't show you're API key when you are sharing your screen with others
    
.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/retreive_activate.png
    :group: planet-order


Select Mosaic
-------------

Now you can select any mosaic in the mosaic dropdown on top of the map. using the :code:`next` or :code:`prev` button will jump to the next/prev mosaic in the list (they are in chronological order)

Once a mosaic is selected the tool will zoom on your AOI and display it in blue. It will add the Planet Lab grid cells (in gold) that are touching the AOI. Each cell of the grid represents 1 image to download. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_rgb.png
    :group: planet-order

Click on the palette btn on the top-left side of the map. This button will expand and show the 4 different color combo available:  

-   **default** the default color combo defined by planet, it can be one of **rgb** or **cir**
-   **rbg** (red, blue, green)
-   **cir** (nir, red, green)
-   **ndvi** a viridis representation of the ndvi index ((nir-red)/(nir+red)) see `wikipedia <https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index>`_

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_cir.png
    :group: planet-order

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_ndvi.png
    :group: planet-order

Download Data
-------------

Once you are satisfied with your mosaic selection, you can click on the :code:`download image` button. This will launch the downloading process of your images from Planet server to you SEPAL folder. 

The images will be stored in the following folder : :code:`/home/<sepalID>/module_results/planet-order/<aoi_name>/<mosaic_name>/`.

.. tip:: 

    In the parent folder (:code:`/home/<sepalID>/module_results/planet-order/<aoi_name>/`) you will find a .geojson file of the planet grid. This can be useful for other tools. 
    
.. note::

    If the requested image is not available (the grid point to water area, the image was to cloudy so filtered by Planet, you don't have the rights to download it.. etc) the image will fail. 
    If the image already exist in your folder it will be skipped. This behaviour allow you to restart a process if your SEPAL conection crashed without restarting all the downloads.

    
