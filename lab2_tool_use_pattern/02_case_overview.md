# Vehicle Sale Preparation Case

## Case Overview
- Case ID: `TU-2026-004`
- Scenario: Recovered Android phone suspected of containing photos and sale-draft activity tied to a stolen vehicle.
- Device: Samsung Galaxy S23 (`Android 14`)
- Incident window (UTC): `2026-01-02T00:00:00Z` to `2026-01-03T03:00:00Z`
- Analysis timezone: `America/New_York`

## Acquisition and Integrity
- Acquisition type: `logical_plus_media_export`
- Acquisition tool: `Magnet AXIOM 8.1`
- Acquisition timestamp (UTC): `2026-01-05T14:22:09Z`
- Original image SHA-256:
  - `8d8f7c95578d2678d12b178f2636d2b566bf1b74153f2f8f7852d1fe6b9f08c4`

## Narrative Summary
After a black SUV with a roof rack was reported stolen on January 2, investigators later recovered a phone believed to have been used by the unknown seller. The staged artifact package includes a gallery index, extracted image metadata, vehicle-attribute detections, and a saved listing draft. Together these artifacts allow students to decide whether the phone contains evidence that the vehicle was photographed and prepared for an online sale.

## Key Observed Event Sequence (UTC)
1. `21:14:03` - `IMG_2044.jpg` captured in the gallery
2. `21:14:05` - detection output marks a black SUV with a roof rack in `IMG_2044.jpg`
3. `21:17:22` - additional gallery images captured with weaker or conflicting matches
4. `21:31:11` - a listing draft titled `black SUV for sale` created with `IMG_2044.jpg` attached
5. `published_at_utc = null` - no artifact shows that the draft was posted live

## Artifact Files
- `artifact_manifest.json`: identifies the case and device, gives the acquisition context, and lists the files in the staged evidence package.
- `media_index.csv`: lists the image files recovered from the phone, including their paths, creation times, sizes, and folders. Use it to find candidate photos.
- `image_metadata.csv`: records each image's capture and edit times, location coordinates, and camera model. Use it to place a candidate image in time and context.
- `vehicle_detections.csv`: records detected vehicle features—such as color, body type, roof rack, and confidence—for each image. Use it to compare a photo with the reported vehicle.
- `listing_drafts.json`: stores saved sale-listing drafts, including their text, attached images, and publication status. Use it to determine whether a vehicle photo was prepared for a sale listing.
- `chain_of_custody.csv`: records acquisition, hash verification, and later handling of the evidence, helping document its integrity.

## Intended Educational Use
This dataset is synthetic and designed to demonstrate a tool-use workflow:
- identify candidate photos
- inspect combined image evidence for one candidate image at a time
- connect media evidence to listing-draft records
- decide whether the evidence supports sale preparation

## What You Should Do Next

In the notebook, you will use local forensic tools to answer one question:

`Does the phone contain confirmed, likely, or unconfirmed evidence that a stolen black SUV was photographed and prepared for an online sale after January 2, 2026?`

Required core tool sequence:

`list_media_files -> inspect_image_evidence -> inspect_listing_records`

Return the same five-part report format in both the manual and `ToolAgent` sections of the notebook:

1. `tool-call log`
2. `strongest timestamp evidence`
3. `strongest vehicle-match evidence`
4. `conclusion label (confirmed, likely, or unconfirmed) with confidence 0-1 per major claim`
5. `explicit evidence mapping and limits`

All required evidence for the core lab is already in the local artifact package above. You do not need a vector database or an external API to complete the main task.

Suggested order for Lab 2:
1. work through `03_lab_notebook.ipynb` for the guided version
2. complete `04_tool_use_assignment.ipynb` for the more independent practice
