from __future__ import annotations
import copy
import importlib
from comfy_api.latest import io

_orig = importlib.import_module('comfy_api_nodes.nodes_runway')

class RunwayImageToVideoNodeGen3a_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen3a')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RunwayImageToVideoNodeGen3a'
        base_display = schema.display_name or 'Runway Image to Video (Gen3a Turbo)'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen3a')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen3a')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen3a')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen3a')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RunwayImageToVideoNodeGen4_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen4')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RunwayImageToVideoNodeGen4'
        base_display = schema.display_name or 'Runway Image to Video (Gen4 Turbo)'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen4')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen4')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen4')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayImageToVideoNodeGen4')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RunwayFirstLastFrameNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RunwayFirstLastFrameNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RunwayFirstLastFrameNode'
        base_display = schema.display_name or 'Runway First-Last-Frame to Video'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayFirstLastFrameNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayFirstLastFrameNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayFirstLastFrameNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayFirstLastFrameNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class RunwayTextToImageNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'RunwayTextToImageNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'RunwayTextToImageNode'
        base_display = schema.display_name or 'Runway Text to Image'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayTextToImageNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayTextToImageNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayTextToImageNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'RunwayTextToImageNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

__all__ = ['RunwayImageToVideoNodeGen3a_ISO', 'RunwayImageToVideoNodeGen4_ISO', 'RunwayFirstLastFrameNode_ISO', 'RunwayTextToImageNode_ISO']