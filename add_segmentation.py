import mobie


def add_segmentation():
    path = '/g/emcf/common/Karel/Mocaeretal2022/figureAmiraV3/Segmentation_mobie_cell1/Mitochondrion/mitochondrion.tif'

    resolution = [0.016] * 3
    chunks = [128] * 3
    scale_factors = [[2, 2, 2]] * 6

    mobie.add_segmentation(path, '', root='./data', dataset_name='photosynthetic_dinoflagellate',
                           segmentation_name='Mitochondrion', menu_name="EM_segmentation",
                           resolution=resolution, scale_factors=scale_factors,
                           chunks=chunks, unit='µm')


if __name__ == '__main__':
    add_segmentation()
