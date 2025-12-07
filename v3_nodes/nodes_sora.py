from __future__ import annotations
import copy
import importlib
from comfy_api.latest import io

_orig = importlib.import_module('comfy_api_nodes.nodes_sora')

class OpenAIVideoSora2_ISO(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        orig_cls = getattr(_orig, 'OpenAIVideoSora2')
        orig_schema = orig_cls.define_schema()
        schema = copy.deepcopy(orig_schema)
        base_node_id = schema.node_id or 'OpenAIVideoSora2'
        base_display = schema.display_name or 'OpenAI Sora - Video'
        schema.node_id = f"{base_node_id}_ISO"
        schema.display_name = f"{base_display}_ISO"
        return schema

    @classmethod
    def execute(cls, **kwargs):
        orig_cls = getattr(_orig, 'OpenAIVideoSora2')
        return orig_cls.execute(**kwargs)

    @classmethod
    def validate_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'OpenAIVideoSora2')
        if hasattr(orig_cls, 'validate_inputs'):
            return orig_cls.validate_inputs(**kwargs)
        return True

    @classmethod
    def fingerprint_inputs(cls, **kwargs):
        orig_cls = getattr(_orig, 'OpenAIVideoSora2')
        if hasattr(orig_cls, 'fingerprint_inputs'):
            return orig_cls.fingerprint_inputs(**kwargs)
        return None

    @classmethod
    def check_lazy_status(cls, **kwargs):
        orig_cls = getattr(_orig, 'OpenAIVideoSora2')
        if hasattr(orig_cls, 'check_lazy_status'):
            return orig_cls.check_lazy_status(**kwargs)
        return [name for name in kwargs if kwargs[name] is None]

__all__ = ['OpenAIVideoSora2_ISO']