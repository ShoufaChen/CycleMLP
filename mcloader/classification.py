import os
from torch.utils.data import Dataset
from .imagenet import ImageNet


class ClassificationDataset(Dataset):
    """Dataset for classification.
    """

    def __init__(self, data_root, split, pipeline=None):
        self.data_source = ImageNet(root=os.path.join(data_root, split),
                                    list_file=os.path.join(data_root, 'meta', '{}.txt'.format(split)),
                                    memcached=True,
                                    mclient_path='/mnt/lustre/share/memcached_client')
        self.pipeline = pipeline

    def __len__(self):
        return self.data_source.get_length()

    def __getitem__(self, idx):
        img, target = self.data_source.get_sample(idx)
        if self.pipeline is not None:
            img = self.pipeline(img)

        return img, target
