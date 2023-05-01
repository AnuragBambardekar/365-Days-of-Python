# pip install aspose.slides

import aspose.slides as slides

# open first PPT
with slides.Presentation("127_Merge_PPTs/Presentation_1.pptx") as pres1:
  
    # open second PPT
    with slides.Presentation("127_Merge_PPTs/Presentation_2.pptx") as pres2:
        
        # loop through slides
        for slide in pres2.slides:
          
            # clone slide
            pres1.slides.add_clone(slide)
        
        # save merged PPT
        pres1.save("127_Merge_PPTs/Combined.pptx", slides.export.SaveFormat.PPTX)