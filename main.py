from PIL import Image
import os

#######ユーザー入力変数#######

# 圧縮したい画像が保存されているフォルダパスを指定
file_path = "before/"

# 圧縮後の画像を保存したいフォルダパスを指定
save_file_path = "after/"

# 保存したい画像フォーマットを指定
save_format_jpg = "jpg"
save_format_png = "png"
save_format_webp = "webp"

# 保存したい画像のファイル名の接尾語を指定
save_filename_suffix = "_comp"

# 「jpg」と「webp」画像の圧縮率の指定
compression_rate_jpg = 50
compression_rate_webp = 50

# 「png」画像の色数の指定
compression_color_num = 256

# 画像の解像度を指定（幅, 高さ）
# 例: (1920, 1080) または None（解像度変更しない場合）
resize_resolution = (2000, 1500)

##########プロセス処理部分##########

# フォルダの区切り文字を取得
Delimiter_path = os.sep

# 圧縮したい画像のファイル名取得
filename_pic_list = os.listdir(file_path)

# for文により、フォルダ内のファイルの数だけ、下記のコードを実行
for filename_pic in filename_pic_list:

    # 元の画像ファイル名をファイル名と拡張子に分割する
    file, ext = os.path.splitext(filename_pic)

    # 画像フォーマットによる場合わけ
    if ext.lower() == '.png':
        # 圧縮したい画像の読み込み
        img = Image.open(file_path + Delimiter_path + filename_pic)
        # 解像度を指定（縮小）
        if resize_resolution:
            img.thumbnail(resize_resolution)
        # 画像の色数を削減
        img = img.convert("P", palette=Image.ADAPTIVE, colors=compression_color_num)
        # 画像を保存
        img.save((save_file_path + Delimiter_path + file + save_filename_suffix +
                 '.' + save_format_png), optimize=True)

    elif ext.lower() in ['.jpg', '.jpeg', '.webp']:
        # 圧縮したい画像の読み込み
        img = Image.open(file_path + Delimiter_path + filename_pic)
        # 解像度を指定（縮小）
        if resize_resolution:
            img.thumbnail(resize_resolution)

        # 保存する画像フォーマットを拡張子により指定
        if ext.lower() in ['.jpg', '.jpeg']:
            save_format = save_format_jpg
            compression_rate = compression_rate_jpg
        elif ext.lower() == '.webp':
            save_format = save_format_webp
            compression_rate = compression_rate_webp

        # 画像を保存
        img.save((save_file_path + Delimiter_path + file + save_filename_suffix +
                 "." + save_format), optimize=True, quality=compression_rate)
