import * as React from "react";
import { createRender, useModelState } from "@anywidget/react";
import { AssetRecordType, Tldraw } from "@tldraw/tldraw";
import "@tldraw/tldraw/tldraw.css";

const render = createRender(() => {
  const [app, setApp] = React.useState(null);
  const [imageDimensions] = useModelState("image_dimensions");
  const [base64img] = useModelState("base64img");

  const handleMount = React.useCallback((app) => {
    setApp(app);
  }, []);

  React.useEffect(() => {
    if (app && base64img && imageDimensions) {
      const [imageWidth, imageHeight] = imageDimensions;
      const assetId = AssetRecordType.createId();
      const placeholderAsset = { id: assetId, typeName: "asset", type: "image", props: { w: imageWidth, h: imageHeight, name: "card-repo.png", isAnimated: false, mimeType: null, src: base64img }, meta: {} };

      app.createAssets([placeholderAsset]);

      // Set the position of the image to the top right corner
      const newX = 900 - imageWidth; // Assuming the container width is 900px
      const newY = 0; // Top position

      app.createShapes([{ type: "image", x: newX, y: newY, props: { w: imageWidth, h: imageHeight, assetId: assetId } }]);
    }
  }, [base64img, app, imageDimensions]);

  return (
    <div style={{position: "relative", width: "1100px", height: "500px" }}>
      <Tldraw autoFocus={false} onMount={handleMount} showMenu={false} showPages={false} />
    </div>
  );
});

export default { render };