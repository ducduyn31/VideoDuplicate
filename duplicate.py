import random
from optparse import OptionParser

import ffmpeg

parser = OptionParser()


def get_video_duration(filename):
    return ffmpeg.probe(filename)['streams'][0]['duration']


def sample_in_k(k, pick_n):
    return random.sample(range(k), pick_n)


if __name__ == '__main__':
    parser.add_option('-i', '--input')
    parser.add_option('-o', '--output')

    (args, _) = parser.parse_args()

    duration = get_video_duration(args.input)
    n_blocks = random.randint(10, 100)
    block_size = float(duration) / n_blocks
    sampled_blocks = sample_in_k(n_blocks, random.randint(0, n_blocks - 2))


    def trim_videos(nth_block):
        return (
            ffmpeg.input(args.input).trim(start=nth_block * block_size, duration=block_size)
        )


    streams = map(trim_videos, sampled_blocks)

    stream = (
        ffmpeg
            .concat(*streams)
            .output(args.output)
            .run(overwrite_output=True)
    )
