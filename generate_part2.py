import json

d = json.load(open('func_descs_needed.json', 'r', encoding='utf-8'))
p = json.load(open('func_params_needed.json', 'r', encoding='utf-8'))

TRANSLATIONS = {}

# Build a mapping from shortened English text to full English text
desc_full = {}
for k in d:
    desc_full[k] = d[k]['en']

param_full = {}
for k in p:
    param_full[k] = p[k]['en']

# Now add all translations using FULL English text as keys
# Function descriptions
TRANSLATIONS[desc_full['func_desc:animcurve_exists']] = "此函数返回给定的动画曲线资产或动画曲线结构是否存在且为有效的动画曲线。"
TRANSLATIONS[desc_full['func_desc:application_surface_is_draw_enabled']] = "如果启用了应用程序表面的自动绘制，此函数将返回true。"
TRANSLATIONS[desc_full['func_desc:array_shift']] = "此函数将移除给定数组中的第一个元素并返回其值。如果数组为空，则返回undefined。"
TRANSLATIONS[desc_full['func_desc:asset_get_ids']] = "此函数返回包含给定类型所有现有资产ID的数组。"
TRANSLATIONS[desc_full['func_desc:asset_has_any_tag']] = "此函数检查是否将一个或多个标记字符串分配给了资源浏览器中的任何资源。您可以提供资源名称（作为字符串）或其资源索引，以及单个标记字符串或每个项目都是单个标记字符串的数组。如果您提供资源索引值，则需要提供可选的资源类型参数（常量），因为不同类型的资源可以具有相同的索引，即使它们不能具有相同的名称。"
TRANSLATIONS[desc_full['func_desc:audio_sound_get_asset']] = "此函数返回用于播放给定声音实例ID的声音资产。\n\n\t\t\t\n\t\t\t声音必须是活动的（即当前正在播放），此函数才能返回正确的值，否则将抛出致命错误。"
TRANSLATIONS[desc_full['func_desc:audio_throw_on_error']] = "此函数可用于切换音频引擎返回的错误是否应抛出中止游戏的运行时错误。"
TRANSLATIONS[desc_full['func_desc:buffer_copy_stride']] = "此函数可用于将多个数据条目从一个缓冲区复制到另一个缓冲区，可以指定源缓冲区和目标缓冲区中各个条目之间的不同步幅。该函数会考虑两个缓冲区的类型。如果缓冲区具有固定大小或不是环绕缓冲区，当读取或写入位置超出缓冲区范围时，复制过程将停止。初始读取和写入位置可以为负数，此时将从给定缓冲区的末尾计算。"
TRANSLATIONS[desc_full['func_desc:buffer_get_surface_depth']] = "使用此函数，您可以将表面深度缓冲区的信息写入给定的缓冲区。缓冲区必须事先创建，并且应该是1字节对齐的缓冲区，足够大以存储要写入的表面数据。"
TRANSLATIONS[desc_full['func_desc:buffer_get_used_size']] = "此函数返回给定缓冲区的已用大小。已用大小是已写入缓冲区的字节数。"
TRANSLATIONS[desc_full['func_desc:buffer_set_surface_depth']] = "此函数将数据从缓冲区复制到表面的深度缓冲区。"
TRANSLATIONS[desc_full['func_desc:camera_copy_transforms']] = "此函数将变换从一个相机复制到另一个相机。"
TRANSLATIONS[desc_full['func_desc:db_to_lin']] = "将分贝(dB)增益转换为线性增益。"
TRANSLATIONS[desc_full['func_desc:dbg_add_font_glyphs']] = "添加TTF字体用于调试渲染。字体应添加到包含文件中，字体大小可以以像素为单位指定，可以选择字体范围（字形必须存在于给定的TTF字体中）：\n\n\t\t\t* -1 - 默认拉丁范围\n\n\t\t\t* 0 - 希腊语\n\n\t\t\t* 1 - 韩语\n\n\t\t\t* 2 - 日语\n\n\t\t\t* 3 - 中文完整\n\n\t\t\t* 4 - 中文简体常用\n\n\t\t\t* 5 - 西里尔字母\n\n\t\t\t* 6 - 泰语\n\n\t\t\t* 7 - 越南语"
TRANSLATIONS[desc_full['func_desc:dbg_button']] = "在当前调试分区中创建按钮，按下按钮时将调用给定的方法；它不分为2列，而是显示在单列中。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_checkbox']] = "在当前调试分区中创建复选框条目，变量将为布尔值true或false。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_color']] = "在当前调试分区中创建颜色条目，变量将为颜色RGB值，无alpha。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_colour']] = "在当前调试分区中创建颜色条目，变量将为颜色RGB值，无alpha。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_control_delete']] = "删除先前创建的dbg_*控件（滑块、按钮、复选框等）。如果控件被删除则返回true，否则返回false。"
TRANSLATIONS[desc_full['func_desc:dbg_control_exists']] = "检查dbg_*控件（滑块、按钮、复选框等）是否存在。如果控件存在则返回true，否则返回false。"
TRANSLATIONS[desc_full['func_desc:dbg_drop_down']] = "在当前调试分区中为值创建下拉菜单，可以使用值数组（带有可选的标签数组）或者值和名称声明为逗号分隔的字符串 - 整数值可以在冒号符号后指定，例如\"Zero,One:10,Two:20\"将创建一个3条目的下拉菜单，根据选择将变量设置为0、10或20。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_get_gamepad_input']] = "获取调试覆盖层中游戏手柄输入的状态，返回-1表示游戏手柄已禁用，返回`all`(-3)表示所有游戏手柄的输入已启用，或其他数字表示正在用于调试覆盖层输入的特定游戏手柄"
TRANSLATIONS[desc_full['func_desc:dbg_same_line']] = "使下一个调试控件放置在当前调试控件的同一行（如果它们是单列控件）"
TRANSLATIONS[desc_full['func_desc:dbg_section']] = "声明一个新的调试分区，它将被添加到当前活动的调试视图中。注意：如果没有活动的调试视图，则会为您创建\"默认\"视图。"
TRANSLATIONS[desc_full['func_desc:dbg_section_delete']] = "删除先前创建的调试分区。如果分区被删除则返回true，否则返回false。"
TRANSLATIONS[desc_full['func_desc:dbg_section_exists']] = "检查调试分区是否仍然存在"
TRANSLATIONS[desc_full['func_desc:dbg_set_section']] = "将当前活动分区设置为给定的分区，任何新控件将被添加到此分区。"
TRANSLATIONS[desc_full['func_desc:dbg_set_view']] = "将当前活动视图设置为给定的视图，任何新控件将被添加到此视图及该视图中的活动分区。"
TRANSLATIONS[desc_full['func_desc:dbg_slider']] = "在当前调试分区中为实数值创建滑块，可以指定最小值和最大值。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_slider_int']] = "在当前调试分区中为整数值创建滑块，可以指定最小值和最大值。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_sprite']] = "在当前调试分区中创建指定精灵和指定索引的精灵视图。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_sprite_button']] = "在当前调试分区中创建按钮，按下按钮时将调用给定的方法；它不分为2列，而是显示在单列中。精灵由给定的引用指定，按钮的宽度和高度以像素为单位指定（如果未指定则使用精灵的宽度和高度）。可以通过指定x和y偏移量以及宽度和高度来显示精灵的一部分（如果未给定则使用整个精灵）。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_text']] = "在当前调试分区中创建文本条目（来自变量），此文本可以多行显示，不分为2列，而是显示在单列中。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_text_input']] = "在当前调试分区中创建文本输入条目。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_text_separator']] = "在当前调试分区中创建文本分隔符条目（来自变量），此文本可以多行显示，不分为2列，而是显示在单列中。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:dbg_view']] = "声明一个新的调试视图，可以从调试覆盖层访问。"
TRANSLATIONS[desc_full['func_desc:dbg_view_delete']] = "删除先前创建的调试视图。如果视图被删除则返回true，否则返回false。"
TRANSLATIONS[desc_full['func_desc:dbg_view_exists']] = "检查调试视图是否仍然存在。"
TRANSLATIONS[desc_full['func_desc:dbg_watch']] = "在当前调试分区中为任何值创建监视，每个值被转换为字符串并显示。注意：如果未声明分区，将创建\"默认\"分区。"
TRANSLATIONS[desc_full['func_desc:debug_input_playback']] = "播放先前录制的输入。"
TRANSLATIONS[desc_full['func_desc:debug_input_record']] = "根据提供的过滤标志开始录制输入。"
TRANSLATIONS[desc_full['func_desc:debug_input_save']] = "保存当前正在录制的输入。这将停止当前录制。"
TRANSLATIONS[desc_full['func_desc:display_get_frequency']] = "此函数返回游戏运行所在显示器的频率（或刷新率）。它将返回以帧每秒为单位的实数值，例如如果您的显示器是60hz，您将得到60，如果是144hz，则得到144，以此类推。"
TRANSLATIONS[desc_full['func_desc:display_get_gui_height']] = "使用此函数可以获取绘制GUI事件中使用的GUI高度（以像素为单位）。"
TRANSLATIONS[desc_full['func_desc:display_set_gui_maximise']] = "此函数将GUI层的分辨率设置为窗口大小，带有可选的缩放和偏移参数。"
TRANSLATIONS[desc_full['func_desc:display_set_gui_maximize']] = "此函数将GUI层的分辨率设置为窗口大小，带有可选的缩放和偏移参数。"
TRANSLATIONS[desc_full['func_desc:draw_clear_depth']] = "此函数可用于清除当前渲染目标的深度缓冲区。"
TRANSLATIONS[desc_full['func_desc:draw_clear_ext']] = "此函数可用于清除当前渲染目标的颜色、深度和模板。"
TRANSLATIONS[desc_full['func_desc:draw_clear_stencil']] = "此函数可用于清除当前渲染目标的模板缓冲区。"
TRANSLATIONS[desc_full['func_desc:draw_enable_skeleton_blend_override']] = "此函数用于启用(true)或禁用(false)当骨骼精灵图集使用预乘alpha时是否覆盖默认混合模式。"
TRANSLATIONS[desc_full['func_desc:draw_enable_skeleton_blendmodes']] = "此函数用于启用(true)或禁用(false)骨骼精灵的逐槽混合模式。"
TRANSLATIONS[desc_full['func_desc:draw_enable_svg_aa']] = "使用此函数可以启用或禁用SVG格式矢量精灵的抗锯齿(AA)。AA简单地平滑矢量图像的边缘以使其外观更好。使用的AA量取决于通过函数draw_set_svg_aa_level()设置的值。默认禁用。"
TRANSLATIONS[desc_full['func_desc:draw_get_circle_precision']] = "此函数获取GameMaker绘制圆形时使用的精度。"
TRANSLATIONS[desc_full['func_desc:draw_get_enable_skeleton_blend_override']] = "如果使用预乘alpha的骨骼精灵图集的默认混合模式被覆盖，此函数返回true，否则返回false。"
TRANSLATIONS[desc_full['func_desc:draw_get_enable_skeleton_blendmodes']] = "此函数返回骨骼精灵的逐槽混合模式是启用(true)还是禁用(false)。"
TRANSLATIONS[desc_full['func_desc:draw_get_svg_aa_level']] = "此函数可用于获取SVG格式矢量精灵的抗锯齿(AA)级别。返回值在0到1之间，显示这些精灵的边缘将被绘制得多\"平滑\"。您可以使用函数draw_set_svg_aa_level()设置AA级别。"
TRANSLATIONS[desc_full['func_desc:draw_set_svg_aa_level']] = "此函数可用于设置SVG格式矢量精灵的抗锯齿(AA)级别。这可以是0到1之间的实数值，将\"平滑\"这些精灵的边缘。注意，要看到此效果，必须首先使用函数draw_enable_svg_aa()启用AA。"
TRANSLATIONS[desc_full['func_desc:ds_grid_to_mp_grid']] = "此函数可用于将DS网格转换为MP网格。您还可以提供可选的谓词函数参数，将DS网格值映射到相应的MP网格值。如果不提供谓词函数，函数将把零值视为空，非零值视为已占用。"
TRANSLATIONS[desc_full['func_desc:effect_create_depth']] = "使用此函数可以在指定深度创建简单效果。\n\n\t\t\t如果效果不是ef_rain或ef_snow，则可以定义x/y位置来创建效果，大小可以是0、1或2，其中0为小，1为中，2为大。"
TRANSLATIONS[desc_full['func_desc:effect_create_layer']] = "使用此函数可以在指定层上创建简单效果。\n\n\t\t\t如果效果不是ef_rain或ef_snow，则可以定义x/y位置来创建效果，大小可以是0、1或2，其中0为小，1为中，2为大。"
TRANSLATIONS[desc_full['func_desc:extension_exists']] = "此函数返回给定名称的扩展是否存在(true)或不存在(false)。"
TRANSLATIONS[desc_full['func_desc:extension_get_option_count']] = "此函数返回给定名称扩展中存在的选项总数。如果提供的扩展名称无效，函数将返回undefined。"
TRANSLATIONS[desc_full['func_desc:extension_get_option_names']] = "此函数返回包含给定名称扩展中所有选项名称的数组。如果提供的扩展名称无效，函数将返回undefined。"
TRANSLATIONS[desc_full['func_desc:extension_get_option_value']] = "此函数返回给定名称扩展中给定选项的值。如果提供的扩展名称无效，函数将返回undefined。"
TRANSLATIONS[desc_full['func_desc:extension_get_options']] = "此函数返回包含给定名称扩展的所有选项及其值的结构。如果提供的扩展名称无效，函数将返回undefined。"
TRANSLATIONS[desc_full['func_desc:extension_get_version']] = "此函数获取给定名称扩展资产的版本，并以\"major.minor.revision\"格式的字符串返回。"
TRANSLATIONS[desc_full['func_desc:flexpanel_calculate_layout']] = "计算选定节点及其子节点的布局。"
TRANSLATIONS[desc_full['func_desc:flexpanel_create_node']] = "创建Flexpanel节点。"
TRANSLATIONS[desc_full['func_desc:flexpanel_delete_node']] = "删除Flexpanel节点。"
TRANSLATIONS[desc_full['func_desc:flexpanel_get_rounding_scale']] = "获取舍入布局值时使用的当前缩放因子。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_get_child']] = "通过索引或名称返回给定节点的子节点，如果超出范围则返回undefined。如果使用名称，则搜索将递归遍历所有子节点，并返回深度优先遍历中的第一个匹配节点。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_get_child_hash']] = "通过名称或名称哈希返回给定节点的子节点。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_get_data']] = "返回给定节点的数据结构。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_get_measure_function']] = "返回给定节点的测量函数。`undefined`表示此节点上未设置测量函数。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_get_name']] = "返回给定节点的名称，如果未设置名称则返回undefined。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_get_num_children']] = "返回给定节点的子节点数量。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_get_parent']] = "返回给定节点的父节点，如果没有父节点则返回undefined。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_get_struct']] = "以结构形式返回给定节点的布局数据。这与可以传递给flexpanel_create_node()的数据相同。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_insert_child']] = "将节点作为子节点插入到传递的父节点中。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_layout_get_position']] = "以结构形式返回计算出的节点布局位置：{left, top, width, height, bottom, right, hadOverflow, direction, paddingLeft, paddingRight, paddingTop, paddingBottom, marginLeft, marginRight, marginTop, marginBottom}。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_remove_all_children']] = "移除节点的所有子节点。\n\n\t\t\t\n\t\t\t注意：子节点不会被删除。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_remove_child']] = "从传递的父节点中移除子节点。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_set_measure_function']] = "设置节点的测量函数。当计算布局且需要测量时（有多种原因可能导致这发生或不发生，例如父级具有绝对宽度和高度），将调用给定的GML函数，它应返回一个结构，包含`width`成员（计算出的宽度）和/或`height`成员（计算出的高度）。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_set_name']] = "设置节点的名称。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_align_content']] = "获取节点内容的对齐方式。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_align_items']] = "获取节点项的对齐方式。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_align_self']] = "获取选定节点的对齐方式。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_aspect_ratio']] = "获取节点的宽高比"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_border']] = "获取选定节点的边框。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_direction']] = "获取选定节点的方向。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_display']] = "获取选定节点的显示设置。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_flex']] = "获取选定节点的flex值。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_flex_basis']] = "获取选定节点的flex基准值。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_flex_direction']] = "获取选定节点的flex方向。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_flex_grow']] = "获取选定节点的flex增长值。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_flex_shrink']] = "获取选定节点的flex收缩值。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_flex_wrap']] = "获取选定节点的flex换行。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_gap']] = "获取选定节点在选定边的间距。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_height']] = "获取选定节点的高度。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_justify_content']] = "获取节点内容的对齐方式"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_margin']] = "获取选定节点的外边距。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_max_height']] = "获取节点的最大高度"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_max_width']] = "获取节点的最大宽度"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_min_height']] = "获取节点的最小高度"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_min_width']] = "获取节点的最小宽度"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_padding']] = "获取选定节点的内边距。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_position']] = "获取节点的样式位置。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_position_type']] = "获取节点的定位类型"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_get_width']] = "获取选定节点的宽度。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_align_content']] = "设置节点内容的对齐方式。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_align_items']] = "设置节点项的对齐方式。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_align_self']] = "设置选定节点的对齐方式。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_aspect_ratio']] = "设置节点的宽高比"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_border']] = "设置选定节点的边框。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_direction']] = "设置选定节点的布局方向。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_display']] = "设置选定节点的显示设置。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_flex']] = "设置选定节点的flex值。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_flex_basis']] = "设置选定节点的flex基准值。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_flex_direction']] = "设置选定节点的flex方向。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_flex_grow']] = "设置选定节点的flex增长值。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_flex_shrink']] = "设置选定节点的flex收缩值。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_flex_wrap']] = "设置选定节点的flex换行。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_gap']] = "设置选定节点在选定槽的间距。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_height']] = "设置选定节点的高度。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_justify_content']] = "设置节点内容的对齐方式"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_margin']] = "设置选定节点的外边距。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_max_height']] = "设置节点的最大高度"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_max_width']] = "设置节点的最大宽度"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_min_height']] = "设置节点的最小高度"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_min_width']] = "设置节点的最小宽度"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_padding']] = "设置选定节点的内边距。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_position']] = "设置节点上的插入位置。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_position_type']] = "设置节点的定位类型。"
TRANSLATIONS[desc_full['func_desc:flexpanel_node_style_set_width']] = "设置选定节点的宽度。"
TRANSLATIONS[desc_full['func_desc:flexpanel_set_rounding_scale']] = "设置舍入布局值时使用的缩放因子。值为0时禁用舍入。"
TRANSLATIONS[desc_full['func_desc:font_cache_glyph']] = "此函数允许您从字体中预缓存字符字形。如果您不使用此函数预缓存字符，它会在首次绘制之前自动缓存。"
TRANSLATIONS[desc_full['func_desc:font_enable_effects']] = "使用此函数，您可以启用或禁用指定字体的内置效果渲染。内置效果仅对启用了SDF的字体有效。"
TRANSLATIONS[desc_full['func_desc:game_change']] = "此函数允许您关闭当前运行的游戏并启动另一个游戏，仅在VM中有效，在某些平台上仅在包构建中有效，在运行/调试中无效。"
TRANSLATIONS[desc_full['func_desc:gamepad_enumerate']] = "目前仅在Android上有效，此函数将枚举游戏手柄以检测新添加的游戏手柄并移除最近移除的游戏手柄，无需BLUETOOTH_CONNECT权限。"
TRANSLATIONS[desc_full['func_desc:gesture_get_rotate_angle']] = "此函数用于获取一对触摸必须超过的角度才能触发旋转开始手势事件。"
TRANSLATIONS[desc_full['func_desc:gpu_get_blendequation']] = "此函数可用于检索当前用于绘制的混合方程。"
TRANSLATIONS[desc_full['func_desc:gpu_get_blendequation_sepalpha']] = "此函数可用于检索当前用于绘制的混合和alpha混合方程。"
TRANSLATIONS[desc_full['func_desc:gpu_get_depth']] = "此函数返回2D绘制函数的当前深度（z坐标）。默认情况下，它将等于当前层的深度，但可以使用gpu_set_depth更改。"
TRANSLATIONS[desc_full['func_desc:gpu_get_scissor']] = "此函数可用于获取当前裁剪区域，返回包含{x, y, w, h}的结构。"
TRANSLATIONS[desc_full['func_desc:gpu_get_sprite_cull']] = "使用此函数可以检查精灵剔除是否启用（返回true）或未启用（返回false）。"
TRANSLATIONS[desc_full['func_desc:gpu_get_stencil_depth_fail']] = "此函数可用于检索模板测试通过但深度测试失败时执行的模板操作。"
TRANSLATIONS[desc_full['func_desc:gpu_get_stencil_enable']] = "此函数可用于检索模板测试当前是否启用（返回true）或未启用（返回false）。"
TRANSLATIONS[desc_full['func_desc:gpu_get_stencil_fail']] = "此函数可用于检索模板测试失败时执行的模板操作。"
TRANSLATIONS[desc_full['func_desc:gpu_get_stencil_func']] = "此函数可用于检索当前的模板测试函数。"
TRANSLATIONS[desc_full['func_desc:gpu_get_stencil_pass']] = "此函数可用于检索模板和深度测试都通过时执行的模板操作。"
TRANSLATIONS[desc_full['func_desc:gpu_get_stencil_read_mask']] = "此函数可用于检索当前的模板测试读取掩码值。"
TRANSLATIONS[desc_full['func_desc:gpu_get_stencil_ref']] = "此函数可用于检索当前的模板测试参考值。"
TRANSLATIONS[desc_full['func_desc:gpu_get_stencil_write_mask']] = "此函数可用于检索当前的模板测试写入掩码值。"
TRANSLATIONS[desc_full['func_desc:gpu_get_tex_filter']] = "使用此函数可以检查纹理过滤（线性插值）是否启用（返回true）或未启用（返回false）。"
TRANSLATIONS[desc_full['func_desc:gpu_get_tex_filter_ext']] = "使用此函数可以检查给定着色器采样器纹理的纹理插值（线性插值）是否启用（返回true）或未启用（返回false）。"
TRANSLATIONS[desc_full['func_desc:gpu_get_tex_repeat']] = "使用此函数可以检查纹理重复是否启用（返回true）或未启用（返回false）。"
TRANSLATIONS[desc_full['func_desc:gpu_get_tex_repeat_ext']] = "使用此函数可以检查给定着色器采样器纹理的纹理重复是否启用（返回true）或未启用（返回false）。"
TRANSLATIONS[desc_full['func_desc:gpu_set_blendequation']] = "使用此函数可以更改从源和目标计算最终像素的方式。"
TRANSLATIONS[desc_full['func_desc:gpu_set_blendequation_sepalpha']] = "此函数与gpu_set_blendequation()相同，但它允许您设置两个单独的方程：第一个用于源和目标的RGB分量，第二个用于alpha分量。"
TRANSLATIONS[desc_full['func_desc:gpu_set_depth']] = "此函数可用于更改2D绘制函数的深度（z坐标）。默认情况下，将使用层的深度。\n\n\t\t\t注意，GameMaker只在开始绘制新层时更改深度，因此您可能希望在绘制完成后恢复原始值（从gpu_get_depth()获取）。"
TRANSLATIONS[desc_full['func_desc:gpu_set_scissor']] = "此函数可用于设置裁剪区域，将所有渲染裁剪到当前渲染目标，所有坐标都在渲染目标坐标系中。注意：所有值都作为整数使用。注意：每个表面和视口都会重置当前裁剪区域（它们不会堆叠）。"
TRANSLATIONS[desc_full['func_desc:gpu_set_sprite_cull']] = "此函数将启用或禁用游戏的精灵剔除（默认启用）。通过关闭精灵剔除，您可以避免例如使用更改精灵绘制位置的自定义着色器时精灵不被绘制等问题。"
TRANSLATIONS[desc_full['func_desc:gpu_set_stencil_depth_fail']] = "此函数可用于设置模板测试通过但深度测试失败时的模板操作。"
TRANSLATIONS[desc_full['func_desc:gpu_set_stencil_enable']] = "此函数可用于禁用或启用模板测试。"
TRANSLATIONS[desc_full['func_desc:gpu_set_stencil_fail']] = "此函数可用于设置模板测试失败时的模板操作。"
TRANSLATIONS[desc_full['func_desc:gpu_set_stencil_func']] = "此函数可用于设置模板测试函数。"
TRANSLATIONS[desc_full['func_desc:gpu_set_stencil_pass']] = "此函数可用于设置模板和深度测试都通过时的模板操作。"
TRANSLATIONS[desc_full['func_desc:gpu_set_stencil_read_mask']] = "此函数可用于设置模板测试读取掩码。"
TRANSLATIONS[desc_full['func_desc:gpu_set_stencil_ref']] = "此函数可用于设置模板测试参考值。"
TRANSLATIONS[desc_full['func_desc:gpu_set_stencil_write_mask']] = "此函数可用于设置模板测试写入掩码。"
TRANSLATIONS[desc_full['func_desc:gpu_set_tex_filter']] = "此函数可用于设置游戏屏幕上绘制的所有图像的纹理过滤（线性插值）。启用(true)时，所有纹理在绘制时将被平滑（这也包括精灵，因为它们也被视为纹理），这意味着当缩放或移动时，如果不是1:1像素比，则会在各个像素上产生\"涂抹\"效果，根据使用的艺术风格可能会使图像显得模糊。如果禁用(false)，则图像在缩放或移动时将基于最近的像素绘制，这可能导致\"块状\"图像。默认值为false，也可以在全局游戏选项中为各个目标平台更改。"
TRANSLATIONS[desc_full['func_desc:gpu_set_tex_filter_ext']] = "此函数可用于在GameMaker中使用着色器时设置单个采样器\"槽\"的线性插值。启用(true)时，采样器纹理将被平滑，禁用(false)时，图像将基于最近的像素绘制。默认值由游戏的全局游戏选项设置，或由函数gpu_set_texfilter()设置的值。"
TRANSLATIONS[desc_full['func_desc:gpu_set_tex_repeat']] = "此函数可用于指示GameMaker在用于模型和图元时纹理是否应重复(true)或不重复(false)。通常纹理的宽度和高度在0到1的范围内，但如果指定大于1的值，默认情况下其余部分不会被绘制（整个纹理将绘制，其中对应于超过1的百分比的部分为\"空\"。因此纹理宽度或高度为2将在一半的空间中绘制纹理，另一半留空）。但是，通过使用此函数将重复设置为true，纹理将在所有模型和图元上自动重复。这些函数的可能用例是在3D中重复纹理，但为了使其工作且不从纹理页的其余部分拉取图像，使用的精灵需要在精灵编辑器中标记为在\"单独纹理页\"上。"
TRANSLATIONS[desc_full['func_desc:gpu_set_tex_repeat_ext']] = "此函数可用于在GameMaker中使用着色器时设置单个采样器\"槽\"是否重复给定纹理。设置为true将在uv坐标超出0-1范围时重复纹理，设置为false表示不重复。这些函数的可能用例是在3D中重复纹理，但为了使其工作且不从纹理页的其余部分拉取图像，使用的精灵需要在精灵编辑器中标记为在\"单独纹理页\"上。"
TRANSLATIONS[desc_full['func_desc:handle_parse']] = "此函数将尝试将字符串转换为句柄数据类型，用于当句柄已转换为字符串而您想将其转换回来的情况。\n\n\t\t\t注意：不对返回的值进行验证，因此不保证其有效。"
TRANSLATIONS[desc_full['func_desc:http_get_connect_timeout']] = "此函数返回HTTP请求使用的连接超时值（以毫秒为单位）。"
TRANSLATIONS[desc_full['func_desc:http_set_connect_timeout']] = "此函数设置HTTP请求使用的连接超时。调用此函数后发出的任何请求都将使用此超时。"
TRANSLATIONS[desc_full['func_desc:is_debug_overlay_open']] = "如果调试覆盖层打开则返回true，否则返回false"
TRANSLATIONS[desc_full['func_desc:is_handle']] = "此函数返回给定变量是否是引用内部类型的句柄。"
TRANSLATIONS[desc_full['func_desc:is_keyboard_used_debug_overlay']] = "如果键盘正被调试覆盖层系统使用则返回true"
TRANSLATIONS[desc_full['func_desc:is_mouse_over_debug_overlay']] = "如果鼠标在调试覆盖层窗口或小部件上，或正被调试子系统使用（即用于拖动）则返回true"
TRANSLATIONS[desc_full['func_desc:keyboard_virtual_set_position']] = "此仅限Windows的函数可用于设置运行游戏的设备上虚拟键盘的位置。传入的坐标为显示坐标（使用application_get_position()查找游戏在此空间中的位置）。"
TRANSLATIONS[desc_full['func_desc:layer_background_change']] = "使用此函数可以设置背景元素的精灵索引。"
TRANSLATIONS[desc_full['func_desc:layer_get_flexpanel_node']] = "此函数检索UI层上的根级flexpanel节点。"
TRANSLATIONS[desc_full['func_desc:layer_get_forced_depth']] = "此函数可用于检索房间内渲染层设置的Z深度。"
TRANSLATIONS[desc_full['func_desc:layer_get_type']] = "您可以使用此函数获取给定层的类型。"
TRANSLATIONS[desc_full['func_desc:layer_particle_alpha']] = "此函数可用于更改粒子系统元素的alpha值。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），然后设置新的alpha值，范围从0（透明）到1（不透明）。"
TRANSLATIONS[desc_full['func_desc:layer_particle_angle']] = "此函数可用于更改粒子系统元素的旋转角度。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），然后设置新的角度（以度为单位）。"
TRANSLATIONS[desc_full['func_desc:layer_particle_blend']] = "此函数可用于更改粒子系统元素的混合颜色。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），然后设置新的混合颜色。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_alpha']] = "此函数可用于检索粒子系统元素的alpha值。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回0（透明）到1（不透明）范围内的值。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_angle']] = "此函数可用于检索粒子系统元素的旋转。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回层元素的旋转角度（以度为单位）。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_blend']] = "此函数可用于检索粒子系统元素的混合颜色。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回层元素的混合颜色。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_id']] = "此函数可用于检索层上粒子系统元素的唯一ID值。您提供层ID（使用layer_create()创建层时获得，或使用层名称配合layer_get_id()获得）和房间编辑器中定义的粒子系统元素名称。函数将返回与该层上粒子系统元素关联的ID值。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_instance']] = "此函数可用于检索与粒子系统元素关联的粒子系统实例的唯一ID。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回与层元素关联的粒子系统实例ID。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_system']] = "此函数可用于检索与粒子系统元素关联的粒子系统资产。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回与层元素关联的粒子系统资产。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_x']] = "此函数可用于检索粒子系统元素在x轴上的位置。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回层元素在x轴上的位置。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_xscale']] = "此函数可用于检索粒子系统元素在x轴上的缩放。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回层元素在x轴上的缩放。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_y']] = "此函数可用于检索粒子系统元素在y轴上的位置。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回层元素在y轴上的位置。"
TRANSLATIONS[desc_full['func_desc:layer_particle_get_yscale']] = "此函数可用于检索粒子系统元素在y轴上的缩放。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），函数返回层元素在y轴上的缩放。"
TRANSLATIONS[desc_full['func_desc:layer_particle_x']] = "此函数可用于更改粒子系统元素在x轴上的位置。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），然后设置要使用的x值（基于房间坐标）。"
TRANSLATIONS[desc_full['func_desc:layer_particle_xscale']] = "此函数可用于更改粒子系统元素在x轴上的缩放。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），然后设置新的缩放值（基于房间坐标）。"
TRANSLATIONS[desc_full['func_desc:layer_particle_y']] = "此函数可用于更改粒子系统元素在y轴上的位置。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），然后设置要使用的y值（基于房间坐标）。"
TRANSLATIONS[desc_full['func_desc:layer_particle_yscale']] = "此函数可用于更改粒子系统元素在y轴上的缩放。您提供粒子系统元素ID（可以使用layer_particle_get_id()获取），然后设置新的缩放值（基于房间坐标）。"
TRANSLATIONS[desc_full['func_desc:layer_text_alpha']] = "此函数控制资产层上文本元素的alpha（透明度）。"
TRANSLATIONS[desc_full['func_desc:layer_text_angle']] = "使用此函数可以更改层上给定文本元素的角度。如果设置的值大于360，将循环到0-359范围内。"
TRANSLATIONS[desc_full['func_desc:layer_text_blend']] = "此函数更改给定文本元素的混合颜色，类似于对象实例的image_blend。"
TRANSLATIONS[desc_full['func_desc:layer_text_charspacing']] = "使用此函数可以更改给定文本元素的字符间距。"
TRANSLATIONS[desc_full['func_desc:layer_text_create']] = "使用此函数可以在指定层上创建新的文本元素。"
TRANSLATIONS[desc_full['func_desc:layer_text_destroy']] = "此函数将销毁给定的文本元素。"
TRANSLATIONS[desc_full['func_desc:layer_text_exists']] = "您可以使用此函数检查任何给定层上是否存在文本元素。"
TRANSLATIONS[desc_full['func_desc:layer_text_font']] = "使用此函数可以更改层上给定文本元素分配的字体资产。"
TRANSLATIONS[desc_full['func_desc:layer_text_frameh']] = "使用此函数可以更改给定文本元素的框架高度。这影响文本的垂直对齐。"
TRANSLATIONS[desc_full['func_desc:layer_text_framew']] = "使用此函数可以更改给定文本元素的框架宽度。这仅在启用换行时影响渲染。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_alpha']] = "此函数可用于获取文本元素的alpha值。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_angle']] = "此函数可用于获取文本元素在房间中的旋转角度。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_blend']] = "此函数可用于获取文本元素的混合颜色。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_charspacing']] = "此函数可用于获取文本元素在房间中的字符间距。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_font']] = "此函数可用于获取文本元素的字体资产引用。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_frameh']] = "此函数可用于获取文本元素在房间中的框架高度。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_framew']] = "此函数可用于获取文本元素在房间中的框架宽度。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_halign']] = "此函数可用于获取文本元素在房间中的水平对齐方式。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_id']] = "此函数可用于检索层上文本元素的唯一ID值。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_linespacing']] = "此函数可用于获取文本元素在房间中的行间距。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_origin']] = "此函数可用于获取文本元素在房间中的框架原点值。您提供文本元素ID（使用layer_text_create()创建文本元素时获得，或使用函数layer_text_get_id()获得），函数将返回原点值。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_paragraphspacing']] = "此函数可用于获取文本元素在房间中的段落间距。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_text']] = "此函数可用于获取文本元素的文本字符串。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_valign']] = "此函数可用于获取文本元素在房间中的垂直对齐方式。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_wrap']] = "此函数可用于获取文本元素在房间中是否启用了换行。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_wrapmode']] = "此函数可用于获取文本元素在房间中的换行模式。您提供文本元素ID（使用layer_text_create()创建文本元素时获得，或使用函数layer_text_get_id()获得），函数将返回换行模式状态。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_x']] = "此函数可用于获取文本元素在房间中的x位置。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_xorigin']] = "此函数可用于获取文本元素在房间中的x原点。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_xscale']] = "此函数可用于获取文本元素在房间中的x缩放。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_y']] = "此函数可用于获取文本元素在房间中的y位置。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_yorigin']] = "此函数可用于获取文本元素在房间中的y原点。"
TRANSLATIONS[desc_full['func_desc:layer_text_get_yscale']] = "此函数可用于获取文本元素在房间中的y缩放。"
TRANSLATIONS[desc_full['func_desc:layer_text_halign']] = "使用此函数可以更改给定文本元素的水平对齐方式。"
TRANSLATIONS[desc_full['func_desc:layer_text_linespacing']] = "使用此函数可以更改给定文本元素的行间距。"
TRANSLATIONS[desc_full['func_desc:layer_text_origin']] = "使用此函数可以设置给定文本元素的框架原点。您提供文本元素ID（使用layer_text_create()创建文本元素时获得，或使用函数layer_text_get_id()获得），然后设置原点值。"
TRANSLATIONS[desc_full['func_desc:layer_text_paragraphspacing']] = "使用此函数可以更改给定文本元素的段落间距。"
TRANSLATIONS[desc_full['func_desc:layer_text_text']] = "使用此函数可以更改层上给定文本元素分配的文本字符串。"
TRANSLATIONS[desc_full['func_desc:layer_text_valign']] = "使用此函数可以更改给定文本元素的垂直对齐方式。"
TRANSLATIONS[desc_full['func_desc:layer_text_wrap']] = "使用此函数可以更改给定文本元素是否启用了换行。"
TRANSLATIONS[desc_full['func_desc:layer_text_wrapmode']] = "使用此函数可以设置给定文本元素的换行模式。您提供文本元素ID（使用layer_text_create()创建文本元素时获得，或使用函数layer_text_get_id()获得），然后设置换行模式。"
TRANSLATIONS[desc_full['func_desc:layer_text_x']] = "此函数控制层上文本元素在房间x轴上的位置。"
TRANSLATIONS[desc_full['func_desc:layer_text_xorigin']] = "使用此函数可以更改给定文本元素原点的x位置。"
TRANSLATIONS[desc_full['func_desc:layer_text_xscale']] = "使用此函数可以更改层上给定文本元素是否应沿x轴缩放。"
TRANSLATIONS[desc_full['func_desc:layer_text_y']] = "此函数控制层上文本元素在房间y轴上的位置。"
TRANSLATIONS[desc_full['func_desc:layer_text_yorigin']] = "使用此函数可以更改给定文本元素原点的y位置。"
TRANSLATIONS[desc_full['func_desc:layer_text_yscale']] = "使用此函数可以更改层上给定文本元素是否应沿y轴缩放。"
TRANSLATIONS[desc_full['func_desc:layer_tilemap_get_colmask']] = "此函数可用于检索正在用作此贴图碰撞遮罩的精灵。"
TRANSLATIONS[desc_full['func_desc:layer_tilemap_set_colmask']] = "此函数可用于设置正在用作此贴图碰撞遮罩的精灵。精灵的尺寸必须与用于贴图集的精灵尺寸匹配。如果函数成功则返回0，如果失败则返回-1"
TRANSLATIONS[desc_full['func_desc:lin_to_db']] = "将线性增益转换为分贝(dB)增益。"
TRANSLATIONS[desc_full['func_desc:mac_refresh_receipt_validation']] = "这将尝试重新验证Mac AppStore收据，并将生成receipt_validation类型的异步系统事件。"
TRANSLATIONS[desc_full['func_desc:matrix_inverse']] = "此函数返回一个新矩阵，它是您传递的矩阵的逆矩阵，或可选地将结果写入您指定的现有矩阵。"
TRANSLATIONS[desc_full['func_desc:nameof']] = "将参数作为字符串返回，在编译时解析。"
TRANSLATIONS[desc_full['func_desc:os_request_permission']] = "此函数向操作系统请求特定权限。在Android上，字符串应格式化为\"android.permission.<permission>\"。在GXgames上，您可以请求\"DeviceMotion\"权限以访问某些浏览器上的方向信息。"
TRANSLATIONS[desc_full['func_desc:part_emitter_delay']] = "使用此函数可以配置发射器在流模式下首次爆发粒子前的延迟。"
TRANSLATIONS[desc_full['func_desc:part_emitter_enable']] = "使用此函数可以启用或禁用粒子发射器。禁用的粒子发射器不会被更新或渲染，也不会产生新粒子。"
TRANSLATIONS[desc_full['func_desc:part_emitter_interval']] = "使用此函数可以配置发射器在流模式下各个粒子爆发之间的间隔。"
TRANSLATIONS[desc_full['func_desc:part_emitter_relative']] = "使用此函数可以启用发射器的相对模式，这意味着发射器爆发或流式发射的粒子数量与其面积成比例。"
TRANSLATIONS[desc_full['func_desc:part_particles_burst']] = "此函数允许您在房间中的任何位置爆发粒子系统资产中定义的所有粒子。"
TRANSLATIONS[desc_full['func_desc:part_system_angle']] = "此函数可用于更改粒子系统的旋转。"
TRANSLATIONS[desc_full['func_desc:part_system_color']] = "此函数可用于更改粒子系统混合的颜色和alpha。"
TRANSLATIONS[desc_full['func_desc:part_system_colour']] = "此函数可用于更改粒子系统混合的颜色和alpha。"
TRANSLATIONS[desc_full['func_desc:part_system_drawit']] = "此函数绘制给定的粒子系统。"
TRANSLATIONS[desc_full['func_desc:part_system_get_info']] = "此函数用于检索给定粒子系统实例的信息。"
TRANSLATIONS[desc_full['func_desc:part_system_global_space']] = "此函数可用于启用全局空间粒子。启用后，当粒子系统移动或旋转时，粒子保持其位置和方向。默认禁用。"
TRANSLATIONS[desc_full['func_desc:part_type_size_x']] = "此函数用于配置粒子大小，类似于part_type_size()，但仅适用于x轴。您可以使用函数part_type_size_y()单独配置y轴上的大小。"
TRANSLATIONS[desc_full['func_desc:part_type_size_y']] = "此函数用于配置粒子大小，类似于part_type_size()，但仅适用于y轴。您可以使用函数part_type_size_x()单独配置x轴上的大小。"
TRANSLATIONS[desc_full['func_desc:part_type_subimage']] = "此函数可用于设置粒子类型使用精灵的自定义子图像（帧）。如果粒子的精灵是动画的，则此子图像将用作动画的起始帧。"
TRANSLATIONS[desc_full['func_desc:particle_add']] = "使用此函数可以从信息结构创建新的粒子系统资产。"
TRANSLATIONS[desc_full['func_desc:particle_delete']] = "使用此函数可以删除粒子系统资产。"
TRANSLATIONS[desc_full['func_desc:particle_exists']] = "使用此函数可以检查给定索引的粒子系统资产是否存在。"
TRANSLATIONS[desc_full['func_desc:particle_get_info']] = "此函数用于检索给定粒子系统资产或实例的信息。"
TRANSLATIONS[desc_full['func_desc:physics_debug']] = "此函数用于切换物理调试消息和错误。"
TRANSLATIONS[desc_full['func_desc:physics_get_friction']] = "此函数获取给定绑定夹具的摩擦值（不是\"基础\"夹具）。"
TRANSLATIONS[desc_full['func_desc:physics_particle_group_get_mass']] = "使用此函数可以检索整组粒子的质量。"
TRANSLATIONS[desc_full['func_desc:physics_raycast']] = "此函数检查给定对象的物理夹具与指定射线的碰撞，它将返回一个结构数组，包含hitPointX、hitPointY（交点的房间坐标）、normalX、normalY（交点的法线）、fraction（交点沿射线的归一化距离）"
TRANSLATIONS[desc_full['func_desc:ref_create']] = "创建对活动变量的调试引用"
TRANSLATIONS[desc_full['func_desc:room_get_info']] = "此函数可用于获取房间的所有信息。它返回一个包含请求数据的结构，房间可能非常大，因此这可能需要很长时间才能完成，可以选择省略一些数据以加快速度。\n\n\t\t\t注意：贴图数据是所有贴图索引的数组，存储为宽度*高度的一维数组，其中x, y条目的索引为(y*width)+x"
TRANSLATIONS[desc_full['func_desc:shader_reset']] = "此函数重置用于绘制的着色器，当您不再希望使用当前着色器（使用shader_set()设置）时应调用此函数。"
TRANSLATIONS[desc_full['func_desc:shader_set_uniform_i_array']] = "此函数设置着色器常量以保存值数组。"
TRANSLATIONS[desc_full['func_desc:show_debug_log']] = "此函数可用于在测试游戏时打开和关闭标准调试日志和控制台，默认禁用。"
TRANSLATIONS[desc_full['func_desc:skeleton_animation_get_event_frames']] = "此函数可用于检索给定动画中给定事件的所有帧。"
TRANSLATIONS[desc_full['func_desc:sphere_is_visible']] = "此函数检查位置x,y,z处半径为r的球体与当前视锥体的碰撞。如果球体与视锥体相交或包含在视锥体内则返回true，如果球体完全在视锥体外则返回false。"
TRANSLATIONS[desc_full['func_desc:sprite_add_ext']] = "使用此函数可以异步添加图像作为精灵，从外部源加载，要加载的图像文件应始终为*.png、*.gif、*.jpg/jpeg或*.json格式（*json文件用于加载使用Spine制作的骨骼动画精灵）。当精灵加载完成后，此函数将生成图像加载异步事件。"
TRANSLATIONS[desc_full['func_desc:sprite_get_convex_hull']] = "此函数用于生成给定精灵的凸包点。函数返回定义凸包点的实数数组。"
TRANSLATIONS[desc_full['func_desc:struct_exists']] = "使用此函数可以检查给定结构中是否存在变量。"
TRANSLATIONS[desc_full['func_desc:struct_exists_from_hash']] = "使用此函数可以检查给定结构中是否存在变量。"
TRANSLATIONS[desc_full['func_desc:struct_foreach']] = "使用此函数可以在结构中的所有成员上执行方法。"
TRANSLATIONS[desc_full['func_desc:struct_get']] = "使用此函数可以从结构中给定命名变量获取值。函数将返回变量持有的值，如果命名变量不存在则返回undefined。"
TRANSLATIONS[desc_full['func_desc:struct_get_from_hash']] = "使用此函数可以从结构中给定命名变量获取值。函数将返回变量持有的值，如果命名变量不存在则返回undefined。"
TRANSLATIONS[desc_full['func_desc:struct_get_names']] = "使用此函数可以检索从结构填充的变量名数组。"
TRANSLATIONS[desc_full['func_desc:struct_names_count']] = "使用此函数可以查找为结构定义的变量总数。函数将返回遇到的变量数的整数值，如果给定ID的结构不存在则返回-1。"
TRANSLATIONS[desc_full['func_desc:struct_remove']] = "使用此函数可以从结构中移除变量。"
TRANSLATIONS[desc_full['func_desc:struct_remove_from_hash']] = "使用此函数可以从结构中移除变量。"
TRANSLATIONS[desc_full['func_desc:struct_set']] = "使用此函数可以设置结构中给定变量的值。如果变量在结构中不存在，它将被创建然后赋值。"
TRANSLATIONS[desc_full['func_desc:struct_set_from_hash']] = "使用此函数可以设置结构中给定变量的值。如果变量在结构中不存在，它将被创建然后赋值。"
TRANSLATIONS[desc_full['func_desc:surface_get_format']] = "此函数返回给定表面的格式。所有格式列在我们的手册中。"
TRANSLATIONS[desc_full['func_desc:surface_get_target_depth']] = "此函数可用于检索深度缓冲区设置为当前缓冲区的表面ID。"
TRANSLATIONS[desc_full['func_desc:surface_get_texture_depth']] = "此函数返回给定表面的深度纹理，如果不存在深度纹理则返回-1。"
TRANSLATIONS[desc_full['func_desc:surface_has_depth']] = "此函数返回给定表面是否具有深度缓冲区（也因此具有模板缓冲区，因为深度缓冲区创建需要启用才能创建模板缓冲区）。"
TRANSLATIONS[desc_full['func_desc:texturegroup_add']] = "添加名为`groupname`的新纹理组，包含单个图像文件或图像文件数组（图像文件可以是`sprite_add`接受的任何格式）。资产将根据最后一个参数中的结构（或json字符串）中的描述创建。可以使用缓冲区代替文件名，使用的任何缓冲区在纹理组删除之前不应被删除，用户负责在此之后删除它们。"
TRANSLATIONS[desc_full['func_desc:texturegroup_delete']] = "删除名为`groupname`的纹理组，只能删除使用texturegroup_add创建的纹理组。"
TRANSLATIONS[desc_full['func_desc:texturegroup_exists']] = "使用此函数可以查看指定名称的纹理组是否存在。"
TRANSLATIONS[desc_full['func_desc:texturegroup_get_names']] = "使用此函数可以检索游戏中包含的所有纹理组的名称。"
TRANSLATIONS[desc_full['func_desc:variable_clone']] = "此函数可以接受任何类型的数据作为其第一个参数，表示要克隆的变量或数据结构（不适用于实例）。第二个参数\"depth\"仅适用于数组和结构，设置克隆过程应执行的深度级别（最大值为128）。"
TRANSLATIONS[desc_full['func_desc:variable_get_hash']] = "使用此函数可以计算给定结构或实例成员的哈希值，以允许更快的访问（参见struct_get_from_hash()和struct_set_from_hash()）。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_get_limit']] = "此函数返回SWF和SVG矢量精灵缓存的当前最大大小。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_get_max_used']] = "此函数返回SWF和SVG矢量精灵缓存使用的最大内存量。如果通过vector_sprite_get_cache_limit()更改缓存大小，此值将被重置。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_get_oldest_entry_age']] = "此函数返回SWF和SVG矢量精灵缓存中最旧条目上次使用的时间。这可用于确定缓存是否设置为适当的大小。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_get_prune_age']] = "此函数返回SWF和SVG矢量精灵缓存中条目在被考虑删除之前可以存在而不被使用的帧数。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_get_prune_fraction']] = "此函数返回每帧尝试清除的SWF和SVG矢量精灵缓存的比例。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_get_used']] = "此函数返回SWF和SVG矢量精灵缓存当前使用的内存量。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_limit']] = "此函数可用于设置用于加速SWF和SVG格式矢量精灵绘制的缓存的最大大小。这可以是0或更大的值。值为0将禁用缓存。更改此值将重置vector_sprite_get_cache_max_used()的返回值。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_prune_age']] = "此函数设置SWF和SVG矢量精灵缓存中的条目在被自动修剪逻辑删除之前必须未被使用的时间。此值以帧为单位测量，应为0或更大。"
TRANSLATIONS[desc_full['func_desc:vector_sprite_cache_prune_fraction']] = "此函数设置每帧尝试清除的SWF和SVG矢量精灵缓存的比例。这可以是0.0到1.0之间的值（值为0.0将禁用自动修剪）。这只会尝试清除比vector_sprite_cache_prune_age()指定的帧数更旧的缓存条目。"
TRANSLATIONS[desc_full['func_desc:vertex_buffer_exists']] = "此函数将检查给定缓冲区是否存在于内存中。如果存在，函数将返回true，否则返回false。"
TRANSLATIONS[desc_full['func_desc:vertex_format_exists']] = "此函数将检查给定顶点格式是否存在于内存中。如果存在，函数将返回true，否则返回false。"
TRANSLATIONS[desc_full['func_desc:vertex_format_get_info']] = "此函数用于检索给定顶点格式的信息。"
TRANSLATIONS[desc_full['func_desc:vertex_submit_ext']] = "此函数将给定顶点缓冲区中的一系列顶点提交到图形管道进行绘制。"
TRANSLATIONS[desc_full['func_desc:vertex_update_buffer_from_buffer']] = "此函数使用常规缓冲区的数据更新顶点缓冲区的内容。顶点缓冲区不能被冻结！"
TRANSLATIONS[desc_full['func_desc:vertex_update_buffer_from_vertex']] = "此函数使用另一个顶点缓冲区的内容更新顶点缓冲区的内容。顶点缓冲区不能被冻结！"
TRANSLATIONS[desc_full['func_desc:wallpaper_set_config']] = "设置动态壁纸的配置"
TRANSLATIONS[desc_full['func_desc:wallpaper_set_subscriptions']] = "设置动态壁纸的订阅"
TRANSLATIONS[desc_full['func_desc:weak_ref_alive']] = "使用此函数可以检查结构的弱引用，以查看它是否仍然\"活动\"。"
TRANSLATIONS[desc_full['func_desc:window_enable_borderless_fullscreen']] = "使用此函数可以启用无边框全屏模式，该模式在切换到全屏时使用无边框窗口而不是让游戏独占使用显示器。\n\n\t\t\t注意，这仅在下次切换到全屏时生效（因此如果游戏当前正在全屏运行，则不会立即更改）。"
TRANSLATIONS[desc_full['func_desc:window_get_borderless_fullscreen']] = "此函数返回全屏模式是使用无边框窗口还是游戏独占控制显示器。"
TRANSLATIONS[desc_full['func_desc:window_get_showborder']] = "返回窗口模式下是否显示窗口周围的边框。"
TRANSLATIONS[desc_full['func_desc:window_minimise']] = "此函数最小化游戏窗口。您可以使用window_restore()恢复它。"
TRANSLATIONS[desc_full['func_desc:window_minimize']] = "此函数最小化游戏窗口。您可以使用window_restore()恢复它。"
TRANSLATIONS[desc_full['func_desc:window_mouse_get_delta_x']] = "返回自上一帧以来鼠标光标在x轴上移动了多少像素。"
TRANSLATIONS[desc_full['func_desc:window_mouse_get_delta_y']] = "返回自上一帧以来鼠标光标在y轴上移动了多少像素。"
TRANSLATIONS[desc_full['func_desc:window_mouse_get_locked']] = "返回鼠标光标是否使用函数window_mouse_set_locked锁定。"
TRANSLATIONS[desc_full['func_desc:window_mouse_set_locked']] = "使用此函数可以启用或禁用鼠标锁定。启用时，鼠标光标被隐藏并锁定在窗口中心。禁用时，鼠标光标显示并解锁。当光标被锁定时，您仍然可以使用函数window_mouse_get_delta_x()和window_mouse_get_delta_y()检索自上一帧以来它移动了多少。"
TRANSLATIONS[desc_full['func_desc:window_post_message']] = "此函数用于GX.games目标，用于向包含游戏的主机窗口发送消息。它接受一个发送到主机iframe的字符串。"
TRANSLATIONS[desc_full['func_desc:window_restore']] = "此函数恢复可能已被用户或使用函数window_minimise()最小化的游戏窗口。"
TRANSLATIONS[desc_full['func_desc:window_set_showborder']] = "设置窗口模式下是否显示窗口周围的边框。"
TRANSLATIONS[desc_full['func_desc:zip_add_file']] = "此函数将在指定的zip文件中添加对指定源文件的引用及所需的目标路径。"
TRANSLATIONS[desc_full['func_desc:zip_create']] = "此函数将创建一个新的zip对象，可以将文件添加到其中。"
TRANSLATIONS[desc_full['func_desc:zip_save']] = "此函数将zip对象保存到指定路径。"
TRANSLATIONS[desc_full['func_desc:zip_unzip_async']] = "此函数将打开存储的zip文件并异步将其内容提取到给定目录。"

# Now add all function parameters using FULL English text
# Collect all unique param English texts
param_en_to_zh = {}
for k in p:
    en = p[k]['en']
    if en not in param_en_to_zh:
        param_en_to_zh[en] = None

# Now assign translations for each unique param English text
param_translations = {
    "The Animation Curve asset or struct that will be checked.": "要检查的动画曲线资产或结构。",
    "The variable that holds the array.": "保存数组的变量。",
    "The type of assets to retrieve an array of.": "要检索的资产类型的数组。",
    "The name of or a reference to the game asset to get the type of.": "要获取类型的游戏资产的名称或引用。",
    "The name of the asset (a string) or its index value (an integer).": "资源的名称(字符串)或其索引值(整数)。",
    "A single asset tag string or an array with various asset tags.": "单个资源标记字符串或具有各种资源标记的数组。",
    "OPTIONAL! The type of asset to check the tags for, only used when supplying an index for the first argument.": "可选！要检查标记的资源类型，仅在为第一个参数提供索引时使用。",
    "The sound asset, as returned by audio_create_stream.": "声音资产，由audio_create_stream返回。",
    "The length for the change in gain in milliseconds.": "增益变化的长度（以毫秒为单位）。",
    "The voice index of the sound.": "声音的语音索引。",
    "Enable or disable throwing.": "启用或禁用抛出。",
    "An input value that can be string, integer, variable or constant.": "可以是字符串、整数、变量或常量的输入值。",
    "The value to convert.": "要转换的值。",
    "The index of the buffer to check.": "要检查的缓冲区索引。",
    "The index of the font.": "字体的索引。",
    "Whether to enable (true) or disable (false) effects rendering for the specified font.": "是否启用(true)或禁用(false)指定字体的效果渲染。",
    "A struct containing any initial values for the font's effect parameters.": "包含字体效果参数初始值的结构。",
    "The FX struct to get the name of": "要获取名称的FX结构",
    "The FX struct to get the parameter from": "要从中获取参数的FX结构",
    "The FX struct to get the parameter names of": "要获取参数名称的FX结构",
    "The FX struct to modify": "要修改的FX结构",
    "Command line parameters to be passed to the new game.": "要传递给新游戏的命令行参数。",
    "The directory in which the new game will launch.": "新游戏将启动的目录。",
    "Optional argument or arguments for the given command.": "给定命令的可选参数。",
    "The blend equation to use": "要使用的混合方程",
    "The alpha blend equation to use": "要使用的alpha混合方程",
    "New drawing depth.": "新的绘制深度。",
    "Enable or disable sprite culling (true / false)": "启用或禁用精灵剔除(true/false)",
    "The operation executed when the stencil test passes but the depth test fails.": "模板测试通过但深度测试失败时执行的操作。",
    "Enable or disable the stencil test (true or false).": "启用或禁用模板测试(true或false)。",
    "The operation executed when the stencil test fails.": "模板测试失败时执行的操作。",
    "The stencil test function.": "模板测试函数。",
    "The operation executed when both stencil and depth test pass.": "模板和深度测试都通过时执行的操作。",
    "A mask that enables or disables reading of individual bits during stencil test.": "在模板测试期间启用或禁用读取各个位的掩码。",
    "The stencil test reference value in range 0 to 255 (inclusive).": "0到255（含）范围内的模板测试参考值。",
    "A mask that enables or disables writing of individual bits during stencil test": "在模板测试期间启用或禁用写入各个位的掩码",
    "The string to convert.": "要转换的字符串。",
    "The connect timeout (in milliseconds)": "连接超时（以毫秒为单位）",
    "The collision space in which to consider instances": "考虑实例的碰撞空间",
    "The collision space in which to consider instances, defaults to the collision space the calling instance is in.": "考虑实例的碰撞空间，默认为调用实例所在的碰撞空间。",
    "The permission to request": "要请求的权限",
    "The index of the emitter.": "发射器的索引。",
    "The particle system that the emitter is in.": "发射器所在的粒子系统。",
    "Enable (true) or disable (false) the particle emitter.": "启用(true)或禁用(false)粒子发射器。",
    "The index of the particle system.": "粒子系统的索引。",
    "The index of the particle type to change.": "要更改的粒子类型的索引。",
    "The particle system asset to delete.": "要删除的粒子系统资产。",
    "Enable or Disable errors and messages": "启用或禁用错误和消息",
    "the half width of the box": "盒子的半宽",
    "the half height of the box": "盒子的半高",
    "reference to the index variable or the name of the variable to dereference.": "索引变量的引用或要解引用的变量名称。",
    "The index of the room.": "房间的索引。",
    "switch on (true) or off (false) the debug overlay.": "打开(true)或关闭(false)调试覆盖层。",
    "The color value to use (A constant, integer or hex value).": "要使用的颜色值（常量、整数或十六进制值）。",
    "The color to set, either an integer, a constant, or a hex value.": "要设置的颜色，可以是整数、常量或十六进制值。",
    "The name (a string file path) of the file to add.": "要添加的文件名（字符串文件路径）。",
    "The name of the struct variable to check for (as a string)": "要检查的结构变量名称（作为字符串）",
    "The struct reference to check": "要检查的结构引用",
    "The struct reference to check.": "要检查的结构引用。",
    "The name of the variable to get": "要获取的变量名称",
    "The struct reference to use": "要使用的结构引用",
    "The name of the variable to remove": "要移除的变量名称",
    "The struct reference to remove the variable from": "要从中移除变量的结构引用",
    "The name of the variable to set": "要设置的变量名称",
    "The value to set the variable to": "要将变量设置为的值",
    "The ID of the surface to get the format of": "要获取格式的表面ID",
    "The ID of the surface to check.": "要检查的表面ID。",
    "The value to be cloned": "要克隆的值",
    "The name of the variable to compute the hash of": "要计算哈希的变量名称",
    "The cache size in bytes.": "缓存大小（以字节为单位）。",
    "Whether to enable borderless fullscreen mode (true) or not (false).": "是否启用无边框全屏模式(true)或不启用(false)。",
    "Enable (true) or disable (false) mouse lock.": "启用(true)或禁用(false)鼠标锁定。",
    "The message to be passed to the host window": "要传递给主机窗口的消息",
    "The color to set for the region.": "要为区域设置的颜色。",
    "Whether to show the window border (true) or not (false).": "是否显示窗口边框(true)或不显示(false)。",
    "The destination path within the zip file.": "zip文件内的目标路径。",
    "The path to the source file to be added.": "要添加的源文件路径。",
    "The zip object which the file should be added to.": "应将文件添加到的zip对象。",
    "The path the zip should be saved to.": "zip应保存到的路径。",
    "The target directory to extract the files to": "要将文件提取到的目标目录",
    "The zip file to open": "要打开的zip文件",
    "The buffer to copy data from.": "要从中复制数据的缓冲区。",
    "The buffer to use.": "要使用的缓冲区。",
    "The data offset value (in bytes).": "数据偏移值（以字节为单位）。",
    "The data offset value.": "数据偏移值。",
    "The offset (in bytes) within the buffer to copy from.": "缓冲区内要从中复制的偏移量（以字节为单位）。",
    "The offset position to copy the data to (in bytes). If negative, then the offset is computed from the end of the buffer.": "复制数据的目标偏移位置（以字节为单位）。如果为负数，则从缓冲区末尾计算偏移量。",
    "The size (in bytes) of data to be copied.": "要复制的数据大小（以字节为单位）。",
    "The number of bytes from the beginning of one entry to the beginning of the following entry in the source buffer. If negative, then the source buffer is traversed backwards.": "源缓冲区中从一个条目开头到下一个条目开头的字节数。如果为负数，则反向遍历源缓冲区。",
    "The desired stride between entries when copied to the destination buffer (in bytes). If negative, then the destination buffer is traversed backwards.": "复制到目标缓冲区时条目之间的所需步幅（以字节为单位）。如果为负数，则反向遍历目标缓冲区。",
    "The size of a single data entry (in bytes). Must be a non-negative value.": "单个数据条目的大小（以字节为单位）。必须为非负值。",
    "The number of data entries to copy. Must be a non-negative value.": "要复制的数据条目数。必须为非负值。",
    "The data offset to start copying from (in bytes). If negative, then the offset is computed from the end of the buffer.": "开始复制的数据偏移量（以字节为单位）。如果为负数，则从缓冲区末尾计算偏移量。",
    "The unique camera ID value for the camera the values will be copied from.": "要从中复制值的相机的唯一相机ID值。",
    "The unique camera ID value for the camera the values will be copied to.": "要将值复制到的相机的唯一相机ID值。",
    "name of the debug section": "调试分区的名称",
    "name of the debug view": "调试视图的名称",
    "handle to the section": "分区的句柄",
    "handle to the view": "视图的句柄",
    "handle to the control": "控件的句柄",
    "reference to the variable to change or array of references to variables": "要更改的变量引用或变量引用数组",
    "reference to the variable to change or array of references to variables or a string to show": "要更改的变量引用或变量引用数组，或要显示的字符串",
    "reference to the variable to change or array of references to variables, or a string to show": "要更改的变量引用或变量引用数组，或要显示的字符串",
    "label to use.": "要使用的标签。",
    "label to use or array of Labels (previous argument needs to be an array)": "要使用的标签或标签数组（前一个参数需要是数组）",
    "minimum value": "最小值",
    "maximum value": "最大值",
    "step value (numbers <=0 indicate no step).": "步进值（数字<=0表示无步进）。",
    "reference to the variable for the sprite index or array of references to variables": "精灵索引的变量引用或变量引用数组",
    "reference to the variable for the image index or array of references to variables": "图像索引的变量引用或变量引用数组",
    "reference to the function to call": "要调用的函数引用",
    "width of button in pixels.": "按钮的宽度（以像素为单位）。",
    "height of button in pixels.": "按钮的高度（以像素为单位）。",
    "width of the view window, default is 500": "视图窗口的宽度，默认为500",
    "height of the view window, default is 400": "视图窗口的高度，默认为400",
    "x position to place the view window, -1 means position anywhere": "放置视图窗口的x位置，-1表示任意位置",
    "y position to place the view window, -1 means position anywhere": "放置视图窗口的y位置，-1表示任意位置",
    "true if view is visible, false otherwise": "如果视图可见则为true，否则为false",
    "true if section is open when created, false if closed, defaults to true": "如果分区在创建时打开则为true，如果关闭则为false，默认为true",
    "alpha level of the debug windows. NOTE: clamped to between 0 and 1": "调试窗口的alpha级别。注意：限制在0到1之间",
    "scale of the debug display. NOTE: clamped to between 0.5 and 4": "调试显示的缩放。注意：限制在0.5到4之间",
    "if true then FPS is opened minimised (default) or false for full size": "如果为true则FPS以最小化方式打开（默认），如果为false则以完整大小打开",
    "if true then FPS is opened minimised (default) or false for full size ": "如果为true则FPS以最小化方式打开（默认），如果为false则以完整大小打开",
    "enabled or disables gamepad input within the debug  overlay (defaults to enabled)": "启用或禁用调试覆盖层中的游戏手柄输入（默认启用）",
    "index of the gamepad to restrict debug overly input to or -1 (default) for all gamepads": "限制调试覆盖层输入的游戏手柄索引，或-1（默认）表示所有游戏手柄",
    "dropdown specifier or array of values": "下拉规范或值数组",
    "alignment of the text separator (0=left, 1=centre, 2=right) defaults to left alignment": "文本分隔符的对齐方式（0=左，1=居中，2=右），默认为左对齐",
    "filename of a TTF file to use": "要使用的TTF字体文件名",
    "size of the font in pixels(default is 13)": "字体大小（以像素为单位，默认为13）",
    "fontRange type (default is -1 - Latin range)": "字体范围类型（默认为-1 - 拉丁范围）",
    "The node.": "节点。",
    "The node to be deleted.": "要删除的节点。",
    "The node to be inserted as a child.": "要作为子节点插入的节点。",
    "The node to be queried.": "要查询的节点。",
    "The node to be removed as a child.": "要作为子节点移除的节点。",
    "The node to be set": "要设置的节点",
    "The node to be set.": "要设置的节点。",
    "The node to set.": "要设置的节点。",
    "The node to start the layout calculations from.": "开始布局计算的节点。",
    "The node whose behaviour should be set.": "要设置行为的节点。",
    "The node whose height should be set.": "要设置高度的节点。",
    "The node whose width should be set.": "要设置宽度的节点。",
    "The parent node.": "父节点。",
    "The index at which to insert the child.": "插入子节点的索引。",
    "The index of the child to get or a string of the name the node has been given.": "要获取的子节点的索引或节点给定的名称字符串。",
    "The hash of the child to get or a string of the name the node has been given.": "要获取的子节点的哈希或节点给定的名称字符串。",
    "The new name to set on the node.": "要在节点上设置的新名称。",
    "The width of the area to calculate the layout over.": "计算布局区域的宽度。",
    "The height of the area to calculate the layout over.": "计算布局区域的高度。",
    "The direction the layout calculation should follow.": "布局计算应遵循的方向。",
    "The function to be executed when calculate layout is done. Accepts the following arguments (width, widthType, height, heightType) the widthType and heightType are either 0 (undefined), 1 (exactly) or 2 (at most).": "布局计算完成时要执行的函数。接受以下参数(width, widthType, height, heightType)，widthType和heightType为0(undefined)、1(exactly)或2(at most)。",
    "Rounding scale factor. Default is 1.": "舍入缩放因子。默认为1。",
    "A struct or JSON string that describes style settings and child nodes to set up this flexpanel.": "描述样式设置和子节点以设置此flexpanel的结构或JSON字符串。",
    "The selected alignment.": "选定的对齐方式。",
    "The selected direction.": "选定的方向。",
    "The selected display.": "选定的显示。",
    "The selected edge.": "选定的边缘。",
    "The selected flex basis value": "选定的flex基准值",
    "The selected gap size": "选定的间距大小",
    "The selected grow factor": "选定的增长因子",
    "The selected gutter (column/row/all).": "选定的槽（列/行/全部）。",
    "The selected height.": "选定的高度。",
    "The selected padding size": "选定的内边距大小",
    "The selected shrink factor": "选定的收缩因子",
    "The selected width.": "选定的宽度。",
    "The selected wrap.": "选定的换行。",
    "The selected border size": "选定的边框大小",
    "The position type to use": "要使用的定位类型",
    "The justification to use": "要使用的对齐方式",
    "The flex value for this": "此项目的flex值",
    "The units to be used": "要使用的单位",
    "The units to use for the value": "值要使用的单位",
    "The value": "值",
    "The value to use": "要使用的值",
    "Whether all child nodes should be deleted (false by default).": "是否应删除所有子节点（默认为false）。",
    "The unique ID value of the layer to target": "要目标的层的唯一ID值",
    "The unique ID value of the layer to target (or the layer name as a string)": "要目标的层的唯一ID值（或层名称作为字符串）",
    "The unique name of the particle system element on the layer as defined in the Room Editor": "房间编辑器中定义的层上粒子系统元素的唯一名称",
    "The unique ID of the particle system element": "粒子系统元素的唯一ID",
    "The unique ID value of the text element to be destroyed": "要销毁的文本元素的唯一ID值",
    "The unique ID value of the text element to change": "要更改的文本元素的唯一ID值",
    "The unique ID value of the text element to check": "要检查的文本元素的唯一ID值",
    "The unique ID value of the text element to get the information from": "要从中获取信息的文本元素的唯一ID值",
    "The unique name of the text element on the layer as defined in the Room Editor": "房间编辑器中定义的层上文本元素的唯一名称",
    "The unique name of the UI layer.": "UI层的唯一名称。",
    "The unique ID value of the layer to get the type of (or the layer name as a string)": "要获取类型的层的唯一ID值（或层名称作为字符串）",
    "The unique ID value of the element to get the type of": "要获取类型的元素的唯一ID值",
    "The alpha for text element, from 0 to 1 (default is 1)": "文本元素的alpha值，从0到1（默认为1）",
    "The angle of the text element (default is 0)": "文本元素的角度（默认为0）",
    "The colour to draw the text element (default is c_white)": "绘制文本元素的颜色（默认为c_white）",
    "The character spacing value (default is 0)": "字符间距值（默认为0）",
    "The font to be used": "要使用的字体",
    "The font to cache a character or glyph from": "要从中缓存字符或字形的字体",
    "The new font to use": "要使用的新字体",
    "The frame height value (default is -1)": "框架高度值（默认为-1）",
    "The frame width value (default is -1)": "框架宽度值（默认为-1）",
    "The line spacing value (default is 0)": "行间距值（默认为0）",
    "The origin value (default is 0)": "原点值（默认为0）",
    "The paragraph spacing value (default is 0)": "段落间距值（默认为0）",
    "The text string to be displayed": "要显示的文本字符串",
    "The new text string to be displayed": "要显示的新文本字符串",
    "The wrapping mode value (default is 0)": "换行模式值（默认为0）",
    "True if wrapping is enabled or false if disabled (default is false)": "如果启用换行则为true，如果禁用则为false（默认为false）",
    "The x position for the text element": "文本元素的x位置",
    "The xorigin value (default is 0)": "x原点值（默认为0）",
    "The xscale value (default is 1)": "x缩放值（默认为1）",
    "The y position for the text element": "文本元素的y位置",
    "The yorigin value (default is 0)": "y原点值（默认为0）",
    "The yscale value (default is 1)": "y缩放值（默认为1）",
    "The new alpha value in range from 0 (transparent) to 1 (opaque)": "新的alpha值，范围从0（透明）到1（不透明）",
    "The new angle of rotation in degrees": "新的旋转角度（以度为单位）",
    "The new blend colour": "新的混合颜色",
    "The new position on the x axis": "x轴上的新位置",
    "The new position on the y axis": "y轴上的新位置",
    "The new scale on the x axis": "x轴上的新缩放",
    "The new scale on the y axis": "y轴上的新缩放",
    "The Id of the tilemap element for which you wish to know the colmask of.": "您想知道碰撞遮罩的贴图元素ID。",
    "The index of the sprite to be used as the collision mask": "要用作碰撞遮罩的精灵索引",
    "The ID of the tile set to use": "要使用的贴图集ID",
    "The index of the emitter to enable or disable.": "要启用或禁用的发射器索引。",
    "Enable (true) or disable (false) relative mode.": "启用(true)或禁用(false)相对模式。",
    "The minimum length of the delay.": "延迟的最小长度。",
    "The maximum length of the delay.": "延迟的最大长度。",
    "The units that the delay is measured in.": "延迟的测量单位。",
    "The minimum length of the interval.": "间隔的最小长度。",
    "The maximum length of the interval.": "间隔的最大长度。",
    "The units that the interval is measured in.": "间隔的测量单位。",
    "The particle system asset to burst.": "要爆发的粒子系统资产。",
    "The x coordinate of where to burst the particles.": "爆发粒子的x坐标。",
    "The y coordinate of where to burst the particles.": "爆发粒子的y坐标。",
    "The index of the particle system to change the rotation of.": "要更改旋转的粒子系统索引。",
    "The new rotation of the particle system in degrees.": "粒子系统的新旋转（以度为单位）。",
    "The index of the particle system to change the color and alpha of.": "要更改颜色和alpha的粒子系统索引。",
    "The index of the particle system to change the colour and alpha of.": "要更改颜色和alpha的粒子系统索引。",
    "The new color with which to blend the particle system. c_white is to display it normally.": "粒子系统混合的新颜色。c_white表示正常显示。",
    "The new colour with which to blend the particle system. c_white is to display it normally.": "粒子系统混合的新颜色。c_white表示正常显示。",
    "The new alpha of the particle system (from 0 to 1 where 0 is transparent and 1 opaque).": "粒子系统的新alpha值（从0到1，其中0为透明，1为不透明）。",
    "The index of the particle system to draw.": "要绘制的粒子系统索引。",
    "The particle system for which information should be retrieved.": "应检索信息的粒子系统。",
    "Enable (true) or disable (false) global space particles.": "启用(true)或禁用(false)全局空间粒子。",
    "The minimum size the particle can start at on the x axis.": "粒子在x轴上可以开始的最小大小。",
    "The maximum size the particle can start at on the x axis.": "粒子在x轴上可以开始的最大大小。",
    "How much the particle should increase or decrease on the x axis per step.": "粒子每步在x轴上应增加或减少多少。",
    "How much should randomly be added or subtracted from the particles size on the x axis per step.": "每步应从粒子大小中随机增加或减去多少（x轴）。",
    "The minimum size the particle can start at on the y axis.": "粒子在y轴上可以开始的最小大小。",
    "The maximum size the particle can start at on the y axis.": "粒子在y轴上可以开始的最大大小。",
    "How much the particle should increase or decrease on the y axis per step.": "粒子每步在y轴上应增加或减少多少。",
    "How much should randomly be added or subtracted from the particles size on the y axis per step.": "每步应从粒子大小中随机增加或减去多少（y轴）。",
    "The sub-image (frame) of the sprite to use.": "要使用的精灵子图像（帧）。",
    "The index of the particle system asset to check for.": "要检查的粒子系统资产索引。",
    "The info struct to create a new particle system asset from.": "用于创建新粒子系统资产的信息结构。",
    "The color blending for the particles.": "粒子的颜色混合。",
    "Instance or object to have the camera target for following": "要让相机跟随的实例或对象",
    "x position of the start of the ray.": "射线起点的x位置。",
    "y position of the start of the ray.": "射线起点的y位置。",
    "instance or object id (or an array of instance or object ids) to check the ray against, these should have physics fixtures": "要检查射线碰撞的实例或对象ID（或实例或对象ID数组），这些应具有物理夹具",
    "proportion of the ray to check, defaults to 1.0, can be set to be smaller or larger": "要检查的射线比例，默认为1.0，可以设置为更小或更大",
    "set to true if you want all hits returned, false if you want the closest hit only - defaults to false": "如果要返回所有碰撞则设置为true，如果只想要最近的碰撞则设置为false - 默认为false",
    "Add instance information to the struct (defaults to true)": "向结构添加实例信息（默认为true）",
    "Add layer element information to the struct (defaults to true), NOTE: you must have layers enabled to get any layer_elements": "向结构添加层元素信息（默认为true），注意：必须启用层才能获取任何层元素",
    "Add room layer information to the struct (defaults to true)": "向结构添加房间层信息（默认为true）",
    "Add room view information to the struct (defaults to true)": "向结构添加房间视图信息（默认为true）",
    "Add tilemap data information to the struct (defaults to true), NOTE: you must have layers and layer_elements enabled to get any tilemap_data (if present)": "向结构添加贴图数据信息（默认为true），注意：必须启用层和层元素才能获取任何贴图数据（如果存在）",
    "if you request the current room then if this is true (default is false) it will report the live data for the current room, otherwise it is the data from the WAD": "如果请求当前房间，如果此值为true（默认为false），它将报告当前房间的实时数据，否则为WAD中的数据",
    "The index of the buffer to copy from.": "要从中复制的缓冲区索引。",
    "The index of the buffer to copy to.": "要复制到的缓冲区索引。",
    "The index of the buffer to use.": "要使用的缓冲区索引。",
    "The argument to check.": "要检查的参数。",
    "The first value to compare.": "要比较的第一个值。",
    "The first value to use in computation.": "计算中要使用的第一个值。",
    "The ID of the surface to get the depth buffer texture of.": "要获取深度缓冲区纹理的表面ID。",
    "The ID of the surface whose depth buffer to use as the current depth buffer.": "深度缓冲区要用作当前深度缓冲区的表面ID。",
    "The index of the surface whose depth buffer to use.": "要使用其深度缓冲区的表面索引。",
    "The name of the texture group to add": "要添加的纹理组名称",
    "The name of the texture group to check": "要检查的纹理组名称",
    "filename or buffer reference for the image file to use or an array of filenames or buffer references for the images": "要使用的图像文件名或缓冲区引用，或图像的文件名或缓冲区引用数组",
    "description of how assets (sprites) are to be created from the image files": "描述如何从图像文件创建资产（精灵）",
    "The number of frames a cache entry can be unused for before being considered for deletion.": "缓存条目在被考虑删除之前可以不被使用的帧数。",
    "The fraction of the cache size to clear (a value between 0.0 and 1.0).": "要清除的缓存大小比例（0.0到1.0之间的值）。",
    "The vertex format for which information should be retrieved.": "应检索信息的顶点格式。",
    "The primitive base type.": "图元基本类型。",
    "The source vertex buffer to copy vertices from.": "要从中复制顶点的源顶点缓冲区。",
    "The destination vertex buffer to copy to.": "要复制到的目标顶点缓冲区。",
    "The vertex buffer to copy to.": "要复制到的顶点缓冲区。",
    "The index of the first vertex to copy from the source vertex buffer.": "要从源顶点缓冲区复制的第一个顶点索引。",
    "The number of vertices to copy.": "要复制的顶点数。",
    "The offset (in bytes) within the vertex buffer to copy to.": "顶点缓冲区内要复制到的偏移量（以字节为单位）。",
    "The index of the first vertex within the destination vertex buffer to copy to.": "目标顶点缓冲区内要复制到的第一个顶点索引。",
    "The index of the first vertex to submit. Must be a positive number.": "要提交的第一个顶点索引。必须为正数。",
    "Number of vertices to submit. Use -1 to submit all vertices after given offset.": "要提交的顶点数。使用-1提交给定偏移量后的所有顶点。",
    "The texture to use (or -1 for no texture).": "要使用的纹理（或-1表示无纹理）。",
    "The viewport to target (0 - 7)": "目标视口(0 - 7)",
    "x coord OR a struct that contains {x, y, w, h}": "x坐标或包含{x, y, w, h}的结构",
    "y coord": "y坐标",
    "width in render target pixels": "渲染目标像素中的宽度",
    "height in render target pixels": "渲染目标像素中的高度",
    "The vertical angle of the field of view.": "视场的垂直角度。",
    "The width of the projection at the near Z position.": "近Z位置处投影的宽度。",
    "The height of the projection at the near Z position.": "近Z位置处投影的高度。",
    "The w component of the transform vector": "变换向量的w分量",
    "The hash of the struct variable to check for": "要检查的结构变量哈希",
    "The hash of the variable being accessed (returned from variable_get_hash())": "正在访问的变量的哈希（由variable_get_hash()返回）",
    "The hash of the variable being removed (returned from 'variable_get_hash')": "正在移除的变量的哈希（由'variable_get_hash'返回）",
    "The hash of the variable being set (returned from 'variable_get_hash')": "正在设置的变量的哈希（由'variable_get_hash'返回）",
    "The struct reference to remove the variable from": "要从中移除变量的结构引用",
    "The struct reference to set": "要设置的结构引用",
    "The variable that holds the struct.": "保存结构的变量。",
    "The unique ID value of the struct to check.": "要检查的结构的唯一ID值。",
    "the function to execute on each member of the struct; the callback function can accept the following arguments - key and value (in this order).": "要在结构的每个成员上执行的函数；回调函数可以接受以下参数 - 键和值（按此顺序）。",
    "The name to convert to string.": "要转换为字符串的名称。",
    "type to store value as, default is string, use \"s\" or \"t\" for string, use \"i\" or \"d\" for integer, use \"f\", \"r\" or \"g\" for real": "存储值的类型，默认为字符串，使用\"s\"或\"t\"表示字符串，使用\"i\"或\"d\"表示整数，使用\"f\"、\"r\"或\"g\"表示实数",
    "Enable or disable the automatic conversion of strings into handles / int64 / nans and infinities. (default is false)": "启用或禁用字符串自动转换为句柄/int64/nan和无穷大。（默认为false）",
    "Index value to use for array references.": "用于数组引用的索引值。",
    "Optionally you can pass in the array in which you would like the result to be stored. This can provide better performance.": "可以选择传入要存储结果的数组。这可以提供更好的性能。",
    "Optionally you can pass in the matrix in which you would like the result to be stored. This can provide better performance.": "可以选择传入要存储结果的矩阵。这可以提供更好的性能。",
    "The matrix to get the inverse of.": "要求逆的矩阵。",
    "The depth to assign the created effect to.": "要将创建的效果分配到的深度。",
    "The layer ID (or name) to assign the created effect to.": "要将创建的效果分配到的层ID（或名称）。",
    "The kind of effect (use one of the constants listed above).": "效果的类型（使用上面列出的常量之一）。",
    "The x positioning of the effect if relevant.": "效果的x定位（如果相关）。",
    "The y positioning of the effect if relevant.": "效果的y定位（如果相关）。",
    "The size of the effect.": "效果的大小。",
    "The colour of the effect.": "效果的颜色。",
    "The setting of the config value.": "配置值的设置。",
    "Config": "配置",
    "Subscriptions": "订阅",
    "reference to the thing to derefernce": "要解引用的事物的引用",
    "The depth to be used during the cloning process (defaults to the maximum of 128)": "克隆过程中要使用的深度（默认为最大值128）",
    "The anti-aliasing value to use from 0 to 1.": "要使用的抗锯齿值，从0到1。",
    "Enable (true) or disable (false) AA for all SVG sprites.": "启用(true)或禁用(false)所有SVG精灵的抗锯齿。",
    "The index of the sprite to generate the convex hull of.": "要生成凸包的精灵索引。",
    "Use this parameter to specify a specific sprite sub-index to use (defaults to 0)": "使用此参数指定要使用的特定精灵子索引（默认为0）",
    "Use this parameter to specify the maximum number of points that can be returned. (If you are intending to generate a physics polygon shape from the points the maximum is 32)": "使用此参数指定可以返回的最大点数。（如果您打算从这些点生成物理多边形形状，最大值为32）",
    "Use to indicate the number of sub-images (1 for a single image or for a *.gif).": "用于指示子图像的数量（1表示单个图像或*.gif）。",
    "Indicates whether the sprite should be loaded to GPU memory.": "指示精灵是否应加载到GPU内存。",
    "Indicate the x position of the origin in the sprite.": "指示精灵中原点的x位置。",
    "Indicate the y position of the origin in the sprite.": "指示精灵中原点的y位置。",
    "xoffset into the sprite in pixels.": "精灵中的x偏移量（以像素为单位）。",
    "yoffset into the sprite in pixels.": "精灵中的y偏移量（以像素为单位）。",
    "width of the sprite in pixels.": "精灵的宽度（以像素为单位）。",
    "height of the sprite in pixels.": "精灵的高度（以像素为单位）。",
    "width to draw the sprite at, if no height given then maintains the correct ratio for the sprite, default is width of the sprite": "绘制精灵的宽度，如果未给定高度则保持精灵的正确比例，默认为精灵的宽度",
    "height draw the sprite at, default is height of the sprite (or uses a given width to maintain correct ratio of width to height)": "绘制精灵的高度，默认为精灵的高度（或使用给定宽度保持正确的宽高比）",
    "The horizontal tiling toggle, which can be true or false": "水平平铺切换，可以为true或false",
    "The vertical tiling toggle, which can be true or false": "垂直平铺切换，可以为true或false",
    "The x position to check.": "要检查的x位置。",
    "The y position to check.": "要检查的y位置。",
    "The z position to check.": "要检查的z位置。",
    "The radius of the sphere to check.": "要检查的球体半径。",
    "The x position to use": "要使用的x位置",
    "The y position to use": "要使用的y位置",
    "The name of the extension": "扩展的名称",
    "The name of your extension asset as a string": "扩展资产的名称作为字符串",
    "The name of the option to read": "要读取的选项名称",
    "The source DS grid.": "源DS网格。",
    "The destination MP grid.": "目标MP网格。",
    "The buffer ID of the buffer to load the map data from.": "要从中加载地图数据的缓冲区ID。",
    "A predicate function (that is passed the: grid value, cell x and cell y) and should return true (cell is ocupied) or false (cell is empty)": "谓词函数（传递：网格值、单元格x和y），应返回true（单元格被占用）或false（单元格为空）",
    "The id of the NEW queue.": "新队列的ID。",
    "The id of the NEW stack.": "新栈的ID。",
    "The id of the list being copied to.": "要复制到的列表ID。",
    "The id of the map you are copying to": "要复制到的映射ID",
    "The id of the priority queue to copy to.": "要复制到的优先队列ID。",
    "filter function called for each value element encoded in the output - function takes 2 arguments (key and value) and returns a value (this is the value that is then placed in the final output)": "对输出中编码的每个值元素调用的过滤函数 - 函数接受2个参数（键和值）并返回一个值（这是放置在最终输出中的值）",
    "filter function called for each value element parsed in the data - function takes 2 arguments (key and value) and returns a value (this is the value that is then placed in the final output)": "对数据中解析的每个值元素调用的过滤函数 - 函数接受2个参数（键和值）并返回一个值（这是放置在最终输出中的值）",
    "The input filter bit mask to use. This can be a combination of `debug_input_filter_` constants.": "要使用的输入过滤位掩码。这可以是`debug_input_filter_`常量的组合。",
    "The path to the file containing a previously recorded input": "包含先前录制输入的文件路径",
    "The path to where the recorded input should be saved to.": "录制输入应保存到的路径。",
    "How long animating the skeleton back to setup pose will take.": "将骨骼动画回到设置姿势需要多长时间。",
    "Whether to reset the skeleton to setup pose (defaults to false).": "是否将骨骼重置为设置姿势（默认为false）。",
    "The colour to clear the current render target with. If undefined, then colour is not cleared. Must be specified if the argument alpha is not undefined.": "用于清除当前渲染目标的颜色。如果为undefined，则不清除颜色。如果参数alpha不为undefined则必须指定。",
    "The alpha value to clear the current render target with. If undefined, then colour is not cleared. Must be specified if the argument col is not undefined.": "用于清除当前渲染目标的alpha值。如果为undefined，则不清除颜色。如果参数col不为undefined则必须指定。",
    "The value to clear the depth buffer with.": "用于清除深度缓冲区的值。",
    "The value to clear the depth buffer with. If undefined, then depth is not cleared.": "用于清除深度缓冲区的值。如果为undefined，则不清除深度。",
    "The value to clear the stencil buffer with.": "用于清除模板缓冲区的值。",
    "The value to clear the stencil buffer with. If undeifned, then stencil is not cleared.": "用于清除模板缓冲区的值。如果为undefined，则不清除模板。",
    "The alignment value (default is 0)": "对齐值（默认为0）",
    "The tile set index to be used": "要使用的贴图集索引",
    "The index of the font to cache a character or glyph from": "要从中缓存字符或字形的字体索引",
    "The index (or character code) of the glyph to cache (see ord()/string_ord_at())": "要缓存的字形的索引（或字符代码）（参见ord()/string_ord_at()）",
    "if true then returned coords in struct are relative to parent, otherwise they are absolute (and include parents position), default is true (so relative coords are returned)": "如果为true，则结构中返回的坐标相对于父级，否则为绝对坐标（包括父级位置），默认为true（因此返回相对坐标）",
    "The type of socket connection to create.": "要创建的套接字连接类型。",
    "x coordinate of the requested position.": "请求位置的x坐标。",
    "y coordinate of the requested position.": "请求位置的y坐标。",
    "The zip object to be saved.": "要保存的zip对象。",
}

# Add all param translations to TRANSLATIONS
for en, zh in param_translations.items():
    TRANSLATIONS[en] = zh

# Write the file
lines = ["TRANSLATIONS = {"]
for en, zh in sorted(TRANSLATIONS.items()):
    en_escaped = en.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t")
    zh_escaped = zh.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t")
    lines.append(f'    "{en_escaped}": "{zh_escaped}",')
lines.append("}")

with open("translations_part2.py", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

# Verify
missing_desc = 0
missing_param = 0
for k in d:
    en = d[k]['en']
    if en not in TRANSLATIONS:
        missing_desc += 1
        print(f'MISSING DESC: {k} ||| {en[:100]}')
for k in p:
    en = p[k]['en']
    if en not in TRANSLATIONS:
        missing_param += 1
        print(f'MISSING PARAM: {k} ||| {en[:100]}')

print(f"\nTotal entries: {len(TRANSLATIONS)}")
print(f"Missing desc: {missing_desc}/{len(d)}, Missing param: {missing_param}/{len(p)}")
