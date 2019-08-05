#!/usr/bin/env python
import args
from image import Offset, decorate_image


if __name__ == '__main__':
    arg = args.parse_args()
    decorate_image(
        arg.input,
        arg.output,
        arg.iterations,
        arg.border,
        Offset(arg.offset_x, arg.offset_y),
        arg.background,
        arg.shadow,
    )
