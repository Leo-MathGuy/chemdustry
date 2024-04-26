package jesse;

import arc.graphics.*;
import mindustry.graphics.Pal;
import mindustry.type.Item;

public class TheIngredients {
    public static class BasicElement {
        Item item;
        String name;

        public BasicElement(Item item) {
            this.name = item.name;
            this.item = item;
        }
    }

    public static BasicElement[] BasicElements;

    /** PURE SOLID COMPOUNDS */
    public static void loadBasicElements() {
        BasicElements = new BasicElement[] {
                new BasicElement(new Item("lithium") {
                    {
                        buildable = true;
                        cost = 0.7f;

                        flammability = 0.2f;
                        explosiveness = 0f;
                        healthScaling = 0.4f;
                        color = TheColors.silveryWhite;
                    }
                }),
                new BasicElement(new Item("beryllium") {
                    {
                        buildable = true;
                        cost = 0.8f;

                        flammability = 0.4f;
                        color = TheColors.silveryWhite;
                        healthScaling = 1.2f;
                    }
                }),
                new BasicElement(new Item("boron") {
                    {
                        buildable = true;
                        cost = 0.5f;

                        flammability = 0.9f;
                        explosiveness = 0.1f;
                        healthScaling = 0.7f;
                        color = TheColors.lessSilvery;
                    }
                }),
                new BasicElement(new Item("graphite") {
                    {
                        buildable = true;
                        cost = 1.4f;

                        healthScaling = 1.5f;
                        color = Pal.darkerGray;
                    }
                }),
                new BasicElement(new Item("diamond") {
                    {
                        buildable = true;
                        cost = 5f;

                        healthScaling = 10f;
                        color = TheColors.diamondBlue;
                    }
                }),
                new BasicElement(new Item("sodium") {
                    {
                        buildable = false;

                        flammability = 0.5f;
                        explosiveness = 0.2f;
                        color = Pal.stoneGray;
                    }
                })
        };
    }
}
