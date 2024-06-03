import os
import shutil
def get_items(directory_path):
    """
    Gets a list of items in the specified directory path.

    :param directory_path: A string representing the path to the directory.
    :return: A list of items (files and directories) in the specified directory.
    """
    try:
        items = os.listdir(directory_path)
    except:
        print("Error in reading the directory")
        exit(

        )
    return items
def spltit(directory_path,split_ratio, size):
    """
    Generate train and test items based on the split ratio and size.

    :param directory_path: The path of the directory containing items.
    :param split_ratio: The ratio at which to split the items into train and test sets.
    :param size: The total number of items to consider.
    :return: Tuple containing train items and test items.
    """
    items = get_items(directory_path)
    req_items = items[:size]
    train_items = req_items[:int(len(req_items)*split_ratio)]
    test_items = req_items[int(len(req_items)*split_ratio):]
    return train_items,test_items
def modify_extensions(filenames, old_extension=".jpg", new_extension=".txt"):
  """
  Modifies the extensions of filenames in a list, replacing the old extension with the new one.

  Args:
      filenames (list): A list of filenames (strings).
      old_extension (str, optional): The extension to replace (default is ".jpg").
      new_extension (str, optional): The new extension to use (default is ".txt").

  Returns:
      list: A new list with filenames having the replaced extensions.
  """

  new_filenames = []
  for filename in filenames:
    base, _ = os.path.splitext(filename)  # Separate filename and extension
    new_filenames.append(f"{base}{new_extension}")
  return new_filenames

def organise(root_path, anot_path, train_items, test_items, images_path):
    """
    Organize the items in the specified directories.

    :param root_path: The path of the directory containing the items to be organised.
    :param anoot_path: The path of the directory where the organised items will be stored.
    :param train_items: The list of train items to be organised.
    :param test_items: The list of test items to be organised.
    """
    image_path = os.path.join(root_path, 'images')
    train_path = os.path.join(image_path, 'train')
    val_path = os.path.join(image_path, 'val')
    try:
        os.makedirs(train_path, exist_ok=True)  # Suppress errors if directory exists
        print(f"Directory '{train_path}' created successfully!")
    except OSError as e:
        print(f"Error creating directory: {e}")
    for item in train_items:
        src = os.path.join(images_path, item)
        dst = os.path.join(train_path, item)
        shutil.copy(src, dst)
    try:
        os.makedirs(val_path, exist_ok=True)  # Suppress errors if directory exists
        print(f"Directory '{val_path}' created successfully!")
    except OSError as e:
        print(f"Error creating directory: {e}")
    for item in test_items:
        src = os.path.join(images_path, item)
        dst = os.path.join(val_path, item)
        shutil.copy(src, dst)
    label_path = os.path.join(root_path, 'labels')
    train_path = os.path.join(label_path, 'train')
    val_path = os.path.join(label_path, 'val')
    try:
        os.makedirs(train_path, exist_ok=True)  # Suppress errors if directory exists
        print(f"Directory '{train_path}' created successfully!")
    except OSError as e:
        print(f"Error creating directory: {e}")
    annot_train_items = modify_extensions(train_items)
    annot_val_items = modify_extensions(test_items)
    for item in annot_train_items:
        src = os.path.join(anot_path, item)
        dst = os.path.join(train_path, item)
        shutil.copy(src, dst)
    try:
        os.makedirs(val_path, exist_ok=True)  # Suppress errors if directory exists
        print(f"Directory '{val_path}' created successfully!")
    except OSError as e:
        print(f"Error creating directory: {e}")
    for item in annot_val_items:
        src = os.path.join(anot_path, item)
        dst = os.path.join(val_path, item)
        shutil.copy(src, dst)


if __name__ == "__main__":
    dest_root_path = "/Users/aftaabhussain/Work/yolo segmentation/B4/data"
    anot_path = "/Users/aftaabhussain/Work/yolo segmentation/B4/Side/txt_annotations"
    images_path = "/Users/aftaabhussain/Work/yolo segmentation/B4/Side/images"
    split_ratio = 0.7
    size = 200
    train_items, test_items = spltit(directory_path=images_path, split_ratio=split_ratio, size=size)
    print(test_items)
    organise(root_path=dest_root_path, anot_path=anot_path, train_items=train_items, test_items=test_items, images_path=images_path)
