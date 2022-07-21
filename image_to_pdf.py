from fpdf import FPDF

def createPdf():
    fpdf = FPDF()
    fpdf= FPDF('P', 'mm', 'A4')

    #add a blank page to the pdf document
    fpdf.add_page()

    ##adding the images
    fpdf.image("images/1.png",x=10,y=10, w=65)
    fpdf.image("https://stickersllamita.com/wp-content/uploads/2022/02/llama-peruana.png",x=75,y=75, w=65)

    ##save the pdf
    fpdf.output("custom.pdf")


if __name__ == "__main__":
    createPdf()

#src https://www.youtube.com/watch?v=dQshrfd5Lpk