import Foundation
import PDFKit
import AppKit

let input = CommandLine.arguments[1]
let output = CommandLine.arguments[2]
guard let doc = PDFDocument(url: URL(fileURLWithPath: input)) else { fatalError("Cannot open PDF") }
try? FileManager.default.createDirectory(atPath: output, withIntermediateDirectories: true)
var allText = ""
for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    allText += "\n\n===== SLIDE \(i + 1) =====\n"
    allText += page.string ?? "[no extractable text]"
    let thumb = page.thumbnail(of: NSSize(width: 960, height: 540), for: .mediaBox)
    guard let data = thumb.tiffRepresentation,
          let rep = NSBitmapImageRep(data: data),
          let png = rep.representation(using: .png, properties: [:]) else { continue }
    try png.write(to: URL(fileURLWithPath: output).appendingPathComponent(String(format: "slide-%03d.png", i + 1)))
}
try allText.write(toFile: output + "/slides.txt", atomically: true, encoding: .utf8)
print("pages=\(doc.pageCount)")
