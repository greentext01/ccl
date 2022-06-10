from caracal.compiler.costumes.build_costumes import build_assets
from caracal.compiler.packaging.bundle_sprite import bundle_sprite
from caracal.compiler.ast_mod import del_cclfiles
from caracal.compiler.blocks.build_blocks import build_blocks
from caracal.compiler.packaging.bundle import bundle
from caracal.compiler.packaging.package import package
from caracal.compiler.run_sprite import run_sprites
from caracal.core.registry import registries


def build():
    run_sprites()
    del_cclfiles()
    
    targets = []
    files = []

    for sprite in registries.get("sprites"):
        blocks = build_blocks(sprite)
        assets, asset_files = build_assets(sprite)
        
        targets.append(bundle_sprite(sprite, blocks, assets))
        files += asset_files
    
    bundled = bundle(targets)
    package(bundled, files)
