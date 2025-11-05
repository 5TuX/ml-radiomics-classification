from IPython.display import display, HTML


def show_image(src, caption="", width="40%", align="center", max_width="400px"):
    """
    Display an image with alignment, caption, and size control in Colab/Jupyter.

    Parameters
    ----------
    src : str
        URL or path to the image.
    caption : str
        Text to display below the image.
    width : str
        Width of the image (e.g. "40%", "300px").
    align : str
        Horizontal alignment: "center", "left", or "right".
    max_width : str
        Maximum width of the image (e.g. "400px").
    """
    justify = {
        "center": "center",
        "left": "flex-start",
        "right": "flex-end",
    }.get(align, "center")

    html = f"""
    <figure style="
        display: flex;
        flex-direction: column;
        align-items: {justify};
        text-align: {align};
        margin: 20px auto;
    ">
        <img src="{src}" style="width: {width}; max-width: {max_width}; height: auto; border-radius: 4px;">
        <figcaption style="margin-top: 8px; max-width: {max_width}; font-size: 0.9em; color: #444;">
            {caption}
        </figcaption>
    </figure>
    """
    display(HTML(html))
