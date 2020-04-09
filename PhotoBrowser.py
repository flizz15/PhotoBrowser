import justpy as jp
from glob import glob


def photo_browser():
    all_container_classes = 'm-1 p-4'
    small_img_container_classes = all_container_classes + ' bg-gray-700'
    images_dir_location_combobox_classes = 'block w-1/4 bg-gray-200 border border-gray-200 text-gray-700 ' \
                                           'py-3 px-4 pr-8 ml-6 rounded leading-tight focus:outline-none ' \
                                           'focus:bg-white focus:border-gray-500 '
    main_container_style = 'position: absolute; top: 500px; width: 100%; margin: 0;'
    images_container_style = 'display:flex; justify-content:space-between; flex-wrap: wrap;'
    main_img_style = 'width: 800px; display: block; margin-left: auto; margin-right: auto; position: fixed;' \
                     'z-index: 2; left: 0; right: 0; margin: 2% auto;'
    small_img_style = 'width: 200px;'

    def small_container_mouseenter(self, msg):
        msg.page.main_img.src = self.child.src
        self.child.style += ' transform: scale(.85);'

    def small_container_mouseleave(self, msg):
        self.child.style = small_img_style
        msg.page.main_img.src = msg.page.main_img_src

    def select_default_img(self, msg):
        msg.page.main_img_src = self.child.src
        for img_cont in msg.page.all_image_containers:
            img_cont.set_class('bg-gray-700')
        self.set_class('bg-red-700')

    def change_images(self, msg):
        msg.page.images_container.delete_components()
        msg.page.small_images = glob(self.value + '*.*')
        msg.page.main_img.src = 'static/' + msg.page.small_images[0]
        load_images()

    wp = jp.WebPage()
    wp.body_classes = 'bg-gray-600'

    small_images_folders = glob('photos/*/')

    try:
        wp.small_images = glob(small_images_folders[0] + '*.*')
        main_img_src = 'static/' + wp.small_images[0]
    except IndexError:
        jp.P(text='Directory photos/ is empty', a=wp, classes='text-5xl m-2 p-2')
        return wp

    main_img = jp.Img(src='', a=wp, style=main_img_style)

    main_container = jp.Div(a=wp, style=main_container_style)
    jp.Label(a=main_container, text='Dir for image src', classes='ml-6')
    images_dir_location_combobox = jp.Select(a=main_container, classes=images_dir_location_combobox_classes)

    for image_folder in small_images_folders:
        if image_folder == small_images_folders[0]:
            jp.Option(value=image_folder, text=image_folder, a=images_dir_location_combobox)
        else:
            jp.Option(value=image_folder, text=image_folder, a=images_dir_location_combobox)

    images_dir_location_combobox.on('change', change_images)

    images_container = jp.Div(a=main_container, classes=all_container_classes, style=images_container_style)

    wp.main_img = main_img
    wp.main_img_src = main_img_src
    wp.images_container = images_container

    def load_images():
        wp.all_image_containers = []
        for i in range(len(wp.small_images)):
            small_img_container = jp.Div(a=images_container, classes=small_img_container_classes,
                                         click=select_default_img, mouseenter=small_container_mouseenter,
                                         mouseleave=small_container_mouseleave,)
            small_img = jp.Img(src=f'/static/{wp.small_images[i]}', a=small_img_container, style=small_img_style,)
            small_img_container.child = small_img
            wp.all_image_containers.append(small_img_container)

        wp.all_image_containers[0].set_class('bg-red-700')

    # load_images()

    return wp


jp.justpy(photo_browser)
