from PIL import Image

im_0_0 = Image.open("C:\programing\Atom_collection\screenshot_programing\IE_0_0.png")
im_0_1 = Image.open("C:\programing\Atom_collection\screenshot_programing\IE_0_1.png")
im_0_2 = Image.open("C:\programing\Atom_collection\screenshot_programing\IE_0_2.png")
im_0_3 = Image.open("C:\programing\Atom_collection\screenshot_programing\IE_0_3.png")

im_0_3 = im_0_3.crop((0,962-3617%962,1980,962))
back = Image.new('RGB',(1920,im_0_0.height+im_0_1.height+im_0_2.height+im_0_3.height))

back.paste(im_0_0,(0,0))
back.paste(im_0_1,(0,im_0_0.height))
back.paste(im_0_2,(0,im_0_0.height+im_0_1.height))
back.paste(im_0_3,(0,im_0_0.height+im_0_1.height+im_0_2.height))


back.save("C:\programing\Atom_collection\screenshot_programing\IE_.png")