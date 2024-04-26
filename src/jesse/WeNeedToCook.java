package jesse;

import arc.*;
import arc.util.*;
import mindustry.*;
import mindustry.content.*;
import mindustry.game.EventType.*;
import mindustry.gen.*;
import mindustry.mod.*;
import mindustry.ui.dialogs.*;

public class WeNeedToCook extends Mod {

    public WeNeedToCook() {
        Log.info("Cooking...");
        Log.info("Jesse we cooked too much");
    }

    @Override
    public void loadContent() {
        Log.info("Jesse how do we cook we don't have anything");
        JesseWtfAreYouTakingAbout.load_overrides();
        Log.info("Thank God Jesse we are ready to cook");
    }

}