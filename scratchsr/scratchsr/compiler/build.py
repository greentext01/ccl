from scratchsr.compiler.costumes.build_costumes import build_assets
from scratchsr.compiler.packaging.bundle_sprite import bundle_sprite
from scratchsr.compiler.ast_mod import del_scsrfiles
from scratchsr.compiler.blocks.build_blocks import build_blocks
from scratchsr.compiler.packaging.bundle import bundle
from scratchsr.compiler.packaging.package import package
from scratchsr.compiler.run_sprite import run_sprites
from scratchsr.util.registry import registries


def build():
    run_sprites()
    del_scsrfiles()
    
    targets = []
    files = []
    current_layer = 0

    for sprite in registries.get("sprites"):
        blocks = build_blocks(sprite)
        assets, asset_files = build_assets(sprite)
        
        targets.append(bundle_sprite(sprite, blocks, assets, current_layer))
        files += asset_files
        current_layer += 1
    
    bundled = bundle(targets)
    package(bundled, files)
