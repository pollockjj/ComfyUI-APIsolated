from __future__ import annotations
import copy
import importlib
from comfy_api.latest import io

_orig = importlib.import_module('comfy_api_nodes.nodes_recraft')

class RecraftColorRGBNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftColorRGBNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftColorRGB'
        base_display = schema.display_name or 'Recraft Color RGB'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftColorRGBNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftColorRGBNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftColorRGBNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftColorRGBNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftControlsNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftControlsNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftControls'
        base_display = schema.display_name or 'Recraft Controls'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftControlsNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftControlsNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftControlsNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftControlsNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftStyleV3RealisticImageNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftStyleV3RealisticImageNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftStyleV3RealisticImage'
        base_display = schema.display_name or 'Recraft Style - Realistic Image'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3RealisticImageNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3RealisticImageNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3RealisticImageNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3RealisticImageNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftStyleV3DigitalIllustrationNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftStyleV3DigitalIllustrationNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftStyleV3DigitalIllustration'
        base_display = schema.display_name or 'Recraft Style - Digital Illustration'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3DigitalIllustrationNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3DigitalIllustrationNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3DigitalIllustrationNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3DigitalIllustrationNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftStyleV3VectorIllustrationNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftStyleV3VectorIllustrationNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftStyleV3VectorIllustrationNode'
        base_display = schema.display_name or 'Recraft Style - Realistic Image'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3VectorIllustrationNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3VectorIllustrationNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3VectorIllustrationNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3VectorIllustrationNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftStyleV3LogoRasterNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftStyleV3LogoRasterNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftStyleV3LogoRaster'
        base_display = schema.display_name or 'Recraft Style - Logo Raster'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3LogoRasterNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3LogoRasterNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3LogoRasterNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleV3LogoRasterNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftStyleInfiniteStyleLibrary_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftStyleInfiniteStyleLibrary')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftStyleV3InfiniteStyleLibrary'
        base_display = schema.display_name or 'Recraft Style - Infinite Style Library'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleInfiniteStyleLibrary')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleInfiniteStyleLibrary')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleInfiniteStyleLibrary')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftStyleInfiniteStyleLibrary')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftTextToImageNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftTextToImageNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftTextToImageNode'
        base_display = schema.display_name or 'Recraft Text to Image'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftTextToImageNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftTextToImageNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftTextToImageNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftTextToImageNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftImageToImageNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftImageToImageNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftImageToImageNode'
        base_display = schema.display_name or 'Recraft Image to Image'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftImageToImageNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftImageToImageNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftImageToImageNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftImageToImageNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftImageInpaintingNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftImageInpaintingNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftImageInpaintingNode'
        base_display = schema.display_name or 'Recraft Image Inpainting'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftImageInpaintingNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftImageInpaintingNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftImageInpaintingNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftImageInpaintingNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftTextToVectorNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftTextToVectorNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftTextToVectorNode'
        base_display = schema.display_name or 'Recraft Text to Vector'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftTextToVectorNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftTextToVectorNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftTextToVectorNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftTextToVectorNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftVectorizeImageNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftVectorizeImageNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftVectorizeImageNode'
        base_display = schema.display_name or 'Recraft Vectorize Image'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftVectorizeImageNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftVectorizeImageNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftVectorizeImageNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftVectorizeImageNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftReplaceBackgroundNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftReplaceBackgroundNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftReplaceBackgroundNode'
        base_display = schema.display_name or 'Recraft Replace Background'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftReplaceBackgroundNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftReplaceBackgroundNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftReplaceBackgroundNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftReplaceBackgroundNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftRemoveBackgroundNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftRemoveBackgroundNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftRemoveBackgroundNode'
        base_display = schema.display_name or 'Recraft Remove Background'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftRemoveBackgroundNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftRemoveBackgroundNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftRemoveBackgroundNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftRemoveBackgroundNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftCrispUpscaleNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftCrispUpscaleNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftCrispUpscaleNode'
        base_display = schema.display_name or 'Recraft Crisp Upscale Image'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftCrispUpscaleNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftCrispUpscaleNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftCrispUpscaleNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftCrispUpscaleNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RecraftCreativeUpscaleNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RecraftCreativeUpscaleNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RecraftCreativeUpscaleNode'
        base_display = schema.display_name or 'Recraft Creative Upscale Image'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftCreativeUpscaleNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftCreativeUpscaleNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftCreativeUpscaleNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RecraftCreativeUpscaleNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

__all__ = ['RecraftColorRGBNode_ISO', 'RecraftControlsNode_ISO', 'RecraftStyleV3RealisticImageNode_ISO', 'RecraftStyleV3DigitalIllustrationNode_ISO', 'RecraftStyleV3VectorIllustrationNode_ISO', 'RecraftStyleV3LogoRasterNode_ISO', 'RecraftStyleInfiniteStyleLibrary_ISO', 'RecraftTextToImageNode_ISO', 'RecraftImageToImageNode_ISO', 'RecraftImageInpaintingNode_ISO', 'RecraftTextToVectorNode_ISO', 'RecraftVectorizeImageNode_ISO', 'RecraftReplaceBackgroundNode_ISO', 'RecraftRemoveBackgroundNode_ISO', 'RecraftCrispUpscaleNode_ISO', 'RecraftCreativeUpscaleNode_ISO']