
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def copy_unique_pdfs(source_dir, target_dir,suffix):
    unique_pdfs = set() # 记录不重复的 PDF 文件名
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            if filename.lower().endswith(suffix):
                filepath = os.path.join(root, filename)
                if filename not in unique_pdfs:
                    # 如果文件名不重复，复制到目标文件夹
                    target_path = os.path.join(target_dir, filename)
                    shutil.copy2(filepath, target_path)
                    unique_pdfs.add(filename)

print('选择两个文件夹\n将会把第一个文件夹中的各类文件，\n提取、去重复,分类后放到第二个文件夹\n')
source_dir = filedialog.askdirectory(title='选择 源 文件夹')
if source_dir == '' :
    print('操作失败，未选择文件夹')
    exit()

target_rootdir = filedialog.askdirectory(title='选择 目标 文件夹') # 设置目标文件夹路径

if target_rootdir == '' :
    print('操作失败，未选择输出文件夹')
    exit()


os.makedirs(os.path.join(target_rootdir, 'xlss'), exist_ok=True)
os.makedirs(os.path.join(target_rootdir, 'pdfs'), exist_ok=True)
os.makedirs(os.path.join(target_rootdir, 'docs'), exist_ok=True)
os.makedirs(os.path.join(target_rootdir, 'docxs'), exist_ok=True)
os.makedirs(os.path.join(target_rootdir, 'ppts'), exist_ok=True)

target_dir = target_rootdir + r'\pdfs' # 设置目标文件夹路径
# 调用函数进行复制操作
copy_unique_pdfs(source_dir, target_dir,".pdf")

target_dir = target_rootdir + r'\xlss' # 设置目标文件夹路径
# 调用函数进行复制操作
copy_unique_pdfs(source_dir, target_dir,".xls")
copy_unique_pdfs(source_dir, target_dir,".xlsx")

target_dir = target_rootdir + r'\docs' # 设置目标文件夹路径
# 调用函数进行复制操作
copy_unique_pdfs(source_dir, target_dir,".doc")


target_dir = target_rootdir + r'\docxs' # 设置目标文件夹路径
copy_unique_pdfs(source_dir, target_dir,".docx")

target_dir = target_rootdir + r'\ppts' # 设置目标文件夹路径
# 调用函数进行复制操作
copy_unique_pdfs(source_dir, target_dir,".ppt")
copy_unique_pdfs(source_dir, target_dir,".pptx")

print('操作完成')
