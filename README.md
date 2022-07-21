# image_to_pdf
## How to use it

1. Install FPDF

2. Stablish the format and units of the PDF

	fpdf= FPDF('P', 'mm', 'A4')

3. We add a page to the pdf

    fpdf.add_page()
    
4. We have two ways of adding an image

4.1 We could add the image with their path

    fpdf.image("images/1.png",x=10,y=10, w=65)
    
4.2 Or we could do it via URL

    fpdf.image("https://stickersllamita.com/wp-content/uploads/2022/02/llama-peruana.png",x=75,y=75, w=65)
    
5. The second and third parameter are the coordenates and the fourth parameter its the width of the image, in this is case is 65mm

6.last we have to save the pdf specifying the name of it

    fpdf.output("custom.pdf")
