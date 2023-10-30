"""pdf 文件转 图片"""

import os
import sys

from pdf2image import convert_from_bytes, convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)


def pdf2img(
    pdf_file: str,
    output_file: str,
    dpi_num: int = 300,
    single_file: bool = False,
    output_folder: str = "./fig-pdf",
):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = convert_from_path(
        pdf_file,
        fmt="png",
        dpi=dpi_num,
        single_file=single_file,
        output_folder=output_folder,
        output_file=output_file,
    )

    return images


if __name__ == "__main__":
    pdf_file = sys.argv[1]
    output_file = sys.argv[2]

    # 单个多页面 pdf 文件转图片
    pdf2img(pdf_file=pdf_file, output_file=output_file)

    # 多个单页面 pdf 文件转图片
    # pdf_path = "pdf_path"
    # pdf_files = [_ for _ in os.listdir(pdf_path) if _.endswith("pdf")]
    # single_file = True

    # for pdf_file in pdf_files:
    #     output_file = f"{pdf_file[:-4]}"
    #     pdf2img(pdf_file=pdf_file, output_file=output_file, single_file=single_file)

    print("\npdf to img convertion is done.")
