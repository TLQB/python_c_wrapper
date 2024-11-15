from setuptools import setup, Extension
from setuptools.command.develop import develop
import py_compile
import os
import shutil

class CustomBuild(develop):
      def run(self):
            if not os.path.exists('powake_loader.py'):
                  raise FileNotFoundError("Không tìm thấy file powake_loader.py")

            # os.makedirs('powake', exist_ok=True)

            # Copy powake.py vào thư mục powake
            # if os.path.exists('powake.py'):
            #       shutil.copy2('powake.py', os.path.join('powake', 'powake.py'))
            #       print(f"Đã copy powake.py vào thư mục powake/")
            # else:
            #       raise FileNotFoundError("Không tìm thấy file powake.py")

            output_path = os.path.join('powake', 'powake_loader.pyc')
            py_compile.compile('powake_loader.py', output_path, optimize=2)

            if os.path.exists(output_path):
                  print(f"Đã compile file .pyc thành công tại: {output_path}")
            else:
                  print("Không thể tạo file .pyc")

            super().run()

# Cấu hình extension module
module = Extension('powake_impl',
                  sources=['powake_impl.c'],
                  extra_compile_args=['-O2'],
                  extra_link_args=['-s'])

setup(
    name='powake',
    version='0.0.1',
    ext_modules=[module],
    package_data={'powakes': ['powake_loader.pyc']},
    packages=['powakes'],
    cmdclass={
        'develop': CustomBuild,
    },
    include_package_data=True,
)