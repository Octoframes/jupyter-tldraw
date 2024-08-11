import * as React from "react";
import { createRender } from "@anywidget/react";
import { AssetRecordType, Tldraw } from "@tldraw/tldraw";
import "@tldraw/tldraw/tldraw.css";

const render = createRender(() => {
  const [app, setApp] = React.useState(null);

  React.useEffect(() => {
    if (!app) return;

    const assetId = AssetRecordType.createId();
    const placeholderAsset = {
      id: assetId,
      typeName: "asset",
      type: "image",
      props: { 
        w: 400, h: 340, name: "chelsea.png", isAnimated: false, mimeType: "image/png", 
        src: "https://raw.githubusercontent.com/scikit-image/scikit-image/main/skimage/data/chelsea.png" 
      },
      meta: {},
    };

    app.createAssets([placeholderAsset]);
    app.createShapes([{ type: "image", props: { w: 300, h: 240, assetId } }]);
  }, [app]);

  return (
    <div style={{ width: "500px", height: "500px" }}>
      <Tldraw autoFocus={false} onMount={setApp} />
    </div>
  );
});

export default { render };