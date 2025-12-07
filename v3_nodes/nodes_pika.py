from __future__ import annotations
import copy
import importlib
from comfy_api.latest import io

_orig = importlib.import_module('comfy_api_nodes.nodes_pika')

class PikaImageToVideo_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'PikaImageToVideo')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'PikaImageToVideoNode2_2'
        base_display = schema.display_name or 'Pika Image to Video'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaImageToVideo')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaImageToVideo')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaImageToVideo')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaImageToVideo')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class PikaTextToVideoNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'PikaTextToVideoNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'PikaTextToVideoNode2_2'
        base_display = schema.display_name or 'Pika Text to Video'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaTextToVideoNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaTextToVideoNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaTextToVideoNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaTextToVideoNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class PikaScenes_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'PikaScenes')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'PikaScenesV2_2'
        base_display = schema.display_name or 'Pika Scenes (Video Image Composition)'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaScenes')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaScenes')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaScenes')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaScenes')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class PikAdditionsNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'PikAdditionsNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'Pikadditions'
        base_display = schema.display_name or 'Pikadditions (Video Object Insertion)'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikAdditionsNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikAdditionsNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikAdditionsNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikAdditionsNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class PikaSwapsNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'PikaSwapsNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'Pikaswaps'
        base_display = schema.display_name or 'Pika Swaps (Video Object Replacement)'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaSwapsNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaSwapsNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaSwapsNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaSwapsNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class PikaffectsNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'PikaffectsNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'Pikaffects'
        base_display = schema.display_name or 'Pikaffects (Video Effects)'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaffectsNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaffectsNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaffectsNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaffectsNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class PikaStartEndFrameNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'PikaStartEndFrameNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'PikaStartEndFrameNode2_2'
        base_display = schema.display_name or 'Pika Start and End Frame to Video'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaStartEndFrameNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaStartEndFrameNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaStartEndFrameNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'PikaStartEndFrameNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

__all__ = ['PikaImageToVideo_ISO', 'PikaTextToVideoNode_ISO', 'PikaScenes_ISO', 'PikAdditionsNode_ISO', 'PikaSwapsNode_ISO', 'PikaffectsNode_ISO', 'PikaStartEndFrameNode_ISO']