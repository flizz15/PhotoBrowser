import justpy as jp
from ntpath import basename
from glob import glob


def photo_browser():
    all_container_classes = 'm-1 p-4'
    small_img_container_classes = all_container_classes + ' bg-gray-700'
    default_combobox_classes = 'block bg-gray-200 border border-gray-200 text-gray-700 ' \
                               'py-3 px-4 pr-8 rounded leading-tight focus:outline-none ' \
                               'focus:bg-white focus:border-gray-500 w-full'
    settings_button_classes = 'm-2 p-2'
    dropdown_menu_classes = 'm-2 p-2 bg-gray-400'
    settings_div_classes = 'w-full'
    main_container_style = 'position: absolute; top: 500px; width: 100%; margin: 0;'
    images_container_style = 'display:flex; justify-content:space-between; flex-wrap: wrap;'
    main_img_style = 'width: 800px; display: block; margin-left: auto; margin-right: auto;' \
                     'z-index: 2; left: 0; right: 0; margin: 2% auto;'
    small_img_style = 'width: 200px;'
    settings_button_style = 'position: absolute;'
    dropdown_menu_style = 'position: absolute; top: 55px; z-index: 3;'
    settings_div_style = 'position: absolute;'

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
        msg.page.main_img_src = msg.page.main_img.src
        print(msg.page.small_images)
        load_images()

    def toggle_show(self, msg):
        self.dropdown_menu.show = not self.dropdown_menu.show

    def set_main_img_position(self, msg):
        if self.checked:
            msg.page.main_img.style = main_img_style
            msg.page.main_img.style += ' position: fixed;'
        else:
            msg.page.main_img.style = main_img_style
            msg.page.main_img.style += ' position: absolute;'

    def change_small_images_content_display(self, msg):
        pass

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
    main_img.show = False

    main_container = jp.Div(a=wp, style=main_container_style)

    settings_div = jp.Div(a=wp, style=settings_div_style, classes=settings_div_classes)

    dropdown_menu = jp.Div(a=settings_div, classes=dropdown_menu_classes, style=dropdown_menu_style)

    jp.Label(a=dropdown_menu, text='Dir for image src*')
    images_dir_location_combobox = jp.Select(a=dropdown_menu, classes=default_combobox_classes)

    jp.Label(a=dropdown_menu, text='Main img pos fixed?')
    main_img_position_checkbox = jp.Input(a=dropdown_menu, type='checkbox', classes='m-1 form-checkbox')
    main_img_position_checkbox.on("change", set_main_img_position)

    jp.Br(a=dropdown_menu)

    jp.Label(a=dropdown_menu, text='Small images content display (not working yet)')
    small_images_content_display_combobox = jp.Select(a=dropdown_menu, classes=default_combobox_classes)
    jp.Option(a=small_images_content_display_combobox, value="photo", text='Photo (default)')
    jp.Option(a=small_images_content_display_combobox, value="text", text='Image name')
    small_images_content_display_combobox.on('change', change_small_images_content_display)

    settings_button = jp.Button(a=settings_div, classes=settings_button_classes, style=settings_button_style)
    settings_button.dropdown_menu = dropdown_menu
    jp.I(a=settings_button, classes='fas fa-cogs fa-2x')
    settings_button.on('click', toggle_show)

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
                                         mouseleave=small_container_mouseleave, )
            small_img = jp.Img(src=f'/static/{wp.small_images[i]}', a=small_img_container, style=small_img_style, )
            small_img_container.child = small_img
            wp.all_image_containers.append(small_img_container)
        wp.main_img.style = main_img_style
        wp.main_img.style += 'position: absolute;'

        wp.all_image_containers[0].set_class('bg-red-700')
        main_img.show = True

    # load_images()

    return wp


jp.justpy(photo_browser)
