#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "A Ghost Writer"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


def main(): # pragma: no cover
    w = World.create_world("ゴーストライター")
    w.config.set_outline('高校の文芸部でやっていたリレー小説に、誰も書いた覚えのない話が書き加えられていた')
    return w.run(
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

