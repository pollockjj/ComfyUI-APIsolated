from __future__ import annotations
import copy
import importlib
from comfy_api.latest import io

_orig = importlib.import_module('comfy_api_nodes.nodes_veo2')

class VeoVideoGenerationNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'VeoVideoGenerationNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'VeoVideoGenerationNode'
        base_display = schema.display_name or 'Google Veo 2 Video Generation'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'VeoVideoGenerationNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'VeoVideoGenerationNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'VeoVideoGenerationNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'VeoVideoGenerationNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class Veo3VideoGenerationNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'Veo3VideoGenerationNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'Veo3VideoGenerationNode'
        base_display = schema.display_name or 'Google Veo 3 Video Generation'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'Veo3VideoGenerationNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'Veo3VideoGenerationNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'Veo3VideoGenerationNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'Veo3VideoGenerationNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

class Veo3FirstLastFrameNode_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'Veo3FirstLastFrameNode')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'Veo3FirstLastFrameNode'
        base_display = schema.display_name or 'Google Veo 3 First-Last-Frame to Video'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'Veo3FirstLastFrameNode')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'Veo3FirstLastFrameNode')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'Veo3FirstLastFrameNode')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'Veo3FirstLastFrameNode')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

__all__ = ['VeoVideoGenerationNode_ISO', 'Veo3VideoGenerationNode_ISO', 'Veo3FirstLastFrameNode_ISO']