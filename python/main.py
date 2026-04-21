import pptx2png


def main():
    pptx2png.topng(
        pptx="pdf/ai-course.pptx",
        output_dir="./images",
    )


if __name__ == "__main__":
    main()
