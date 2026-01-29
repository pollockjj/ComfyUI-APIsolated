from __future__ import annotations

from comfy_api.latest import ComfyExtension, IO

from .nodes_bfl import BFLExtension_ISO
from .nodes_bytedance import ByteDanceExtension_ISO
from .nodes_gemini import GeminiExtension_ISO
from .nodes_ideogram import IdeogramExtension_ISO
from .nodes_kling import KlingExtension_ISO
from .nodes_ltxv import LtxvApiExtension_ISO
from .nodes_luma import LumaExtension_ISO
from .nodes_minimax import MinimaxExtension_ISO
from .nodes_moonvalley import MoonvalleyExtension_ISO
from .nodes_openai import OpenAIExtension_ISO
from .nodes_pika import PikaApiNodesExtension_ISO
from .nodes_pixverse import PixVerseExtension_ISO
from .nodes_recraft import RecraftExtension_ISO
from .nodes_rodin import Rodin3DExtension_ISO
from .nodes_runway import RunwayExtension_ISO
from .nodes_sora import OpenAISoraExtension_ISO
from .nodes_stability import StabilityExtension_ISO
from .nodes_topaz import TopazExtension_ISO
from .nodes_tripo import TripoExtension_ISO
from .nodes_veo2 import VeoExtension_ISO
from .nodes_vidu import ViduExtension_ISO
from .nodes_wan import WanApiExtension_ISO
from .nodes_zero_copy_test import ZeroCopyTestExtension_ISO

__all__ = ['comfy_entrypoint']

class CompositeAPIExtension(ComfyExtension):
    def __init__(self):
        self.extensions = []
    
    async def get_node_list(self) -> list[type[IO.ComfyNode]]:
        nodes = []
        for ext in self.extensions:
            nodes.extend(await ext.get_node_list())
        return nodes

async def comfy_entrypoint():
    composite = CompositeAPIExtension()
    composite.extensions = [
        BFLExtension_ISO(),
        ByteDanceExtension_ISO(),
        GeminiExtension_ISO(),
        IdeogramExtension_ISO(),
        KlingExtension_ISO(),
        LtxvApiExtension_ISO(),
        LumaExtension_ISO(),
        MinimaxExtension_ISO(),
        MoonvalleyExtension_ISO(),
        OpenAIExtension_ISO(),
        PikaApiNodesExtension_ISO(),
        PixVerseExtension_ISO(),
        RecraftExtension_ISO(),
        Rodin3DExtension_ISO(),
        RunwayExtension_ISO(),
        OpenAISoraExtension_ISO(),
        StabilityExtension_ISO(),
        TopazExtension_ISO(),
        TripoExtension_ISO(),
        VeoExtension_ISO(),
        ViduExtension_ISO(),
        WanApiExtension_ISO(),
        ZeroCopyTestExtension_ISO(),
    ]
    return composite