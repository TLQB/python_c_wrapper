import sys
from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location
import powake_impl

class ALoader(Loader):

    def exec_module(self, module):
        # Thực thi module gốc
        exec('def func(): pass\ndef add_license(license_key): pass', module.__dict__)
        # Override func với implementation từ C
        original_add_license = module.add_license
        original_func = module.func

        def wrapped_add_license(license_key):
            powake_impl.add_license(license_key)
            return original_add_license(license_key)
            
        def wrapped_func(*args, **kwargs):
            powake_impl.func()
            return original_func(*args, **kwargs)
        
        module.add_license = wrapped_add_license
        module.func = wrapped_func

class AFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname == "powake":
            return spec_from_file_location(fullname, "powake.py", loader=ALoader())
        return None

# Thêm custom finder vào sys.meta_path ngay trong module a
sys.meta_path.insert(0, AFinder())