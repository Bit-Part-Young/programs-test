import os

from pdf2image import convert_from_bytes, convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)


def single_pdf2img(pdf_file, output_file, dpi_num=300):
    images = convert_from_path(
        pdf_file,
        fmt="png",
        dpi=dpi_num,
        single_file=False,
        output_folder="./fig-pdf",
        output_file=output_file,
    )


def multi_pdf2img(pdf_path, dpi_num=300):
    pdf_files = [_ for _ in os.listdir(pdf_path) if _.endswith("pdf")]

    for pdf_file in pdf_files:
        images = convert_from_path(
            pdf_file,
            fmt="png",
            dpi=dpi_num,
            single_file=False,
            output_folder="./fig-pdf",
            output_file=f"{pdf_file[:-4]}-dpi-{dpi_num}",
        )


if __name__ == "__main__":
    dpi_num = 300
    pdf_file = "pdf_file"
    output_file = "pdf_fig"
    single_pdf2img(pdf_file, output_file, dpi_num)

    # pdf_path = "pdf_path"
    # multi_pdf2img(pdf_path, dpi_num)

    print("work is done.")
