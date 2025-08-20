globals.css:
@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

:root {
  /* Updated color tokens to match GitRules design brief */
  --background: oklch(1 0 0); /* #ffffff */
  --foreground: oklch(0.35 0 0); /* #4b5563 */
  --card: oklch(0.98 0 0); /* #f9fafb */
  --card-foreground: oklch(0.35 0 0); /* #4b5563 */
  --popover: oklch(1 0 0); /* #ffffff */
  --popover-foreground: oklch(0.35 0 0); /* #4b5563 */
  --primary: oklch(0.55 0.15 200); /* #0891b2 cyan-600 */
  --primary-foreground: oklch(1 0 0); /* #ffffff */
  --secondary: oklch(0.65 0.25 330); /* #ec4899 pink */
  --secondary-foreground: oklch(1 0 0); /* #ffffff */
  --muted: oklch(0.98 0 0); /* #f9fafb */
  --muted-foreground: oklch(0.35 0 0); /* #4b5563 */
  --accent: oklch(0.65 0.25 330); /* #ec4899 pink */
  --accent-foreground: oklch(1 0 0); /* #ffffff */
  --destructive: oklch(0.5 0.25 15); /* #be123c */
  --destructive-foreground: oklch(1 0 0); /* #ffffff */
  --border: oklch(0.92 0 0); /* #e5e7eb */
  --input: oklch(0.98 0 0); /* #f9fafb */
  --ring: oklch(0.55 0.15 200 / 0.5); /* rgba(8, 145, 178, 0.5) */
  --chart-1: oklch(0.55 0.15 200); /* #0891b2 */
  --chart-2: oklch(0.65 0.25 330); /* #ec4899 */
  --chart-3: oklch(0.35 0 0); /* #4b5563 */
  --chart-4: oklch(0.98 0 0); /* #f9fafb */
  --chart-5: oklch(0.5 0.25 15); /* #be123c */
  --radius: 0.5rem;
  --sidebar: oklch(0.98 0 0); /* #f9fafb */
  --sidebar-foreground: oklch(0.35 0 0); /* #4b5563 */
  --sidebar-primary: oklch(0.55 0.15 200); /* #0891b2 */
  --sidebar-primary-foreground: oklch(1 0 0); /* #ffffff */
  --sidebar-accent: oklch(0.65 0.25 330); /* #ec4899 */
  --sidebar-accent-foreground: oklch(1 0 0); /* #ffffff */
  --sidebar-border: oklch(0.92 0 0); /* #e5e7eb */
  --sidebar-ring: oklch(0.55 0.15 200 / 0.5); /* rgba(8, 145, 178, 0.5) */
  --font-dm-sans: "DM Sans", sans-serif;
  --font-space-grotesk: "Space Grotesk", serif;
}

.dark {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  --card: oklch(0.145 0 0);
  --card-foreground: oklch(0.985 0 0);
  --popover: oklch(0.145 0 0);
  --popover-foreground: oklch(0.985 0 0);
  --primary: oklch(0.985 0 0);
  --primary-foreground: oklch(0.205 0 0);
  --secondary: oklch(0.269 0 0);
  --secondary-foreground: oklch(0.985 0 0);
  --muted: oklch(0.269 0 0);
  --muted-foreground: oklch(0.708 0 0);
  --accent: oklch(0.269 0 0);
  --accent-foreground: oklch(0.985 0 0);
  --destructive: oklch(0.396 0.141 25.723);
  --destructive-foreground: oklch(0.637 0.237 25.331);
  --border: oklch(0.269 0 0);
  --input: oklch(0.269 0 0);
  --ring: oklch(0.439 0 0);
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
  --chart-3: oklch(0.769 0.188 70.08);
  --chart-4: oklch(0.627 0.265 303.9);
  --chart-5: oklch(0.645 0.246 16.439);
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.269 0 0);
  --sidebar-accent-foreground: oklch(0.985 0 0);
  --sidebar-border: oklch(0.269 0 0);
  --sidebar-ring: oklch(0.439 0 0);
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-destructive-foreground: var(--destructive-foreground);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);
  --font-sans: var(--font-dm-sans);
  --font-serif: var(--font-space-grotesk);
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
}

layout.tsx:
import type React from "react"
import type { Metadata } from "next"
import { Space_Grotesk, DM_Sans } from "next/font/google"
import "./globals.css"

const spaceGrotesk = Space_Grotesk({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-space-grotesk",
})

const dmSans = DM_Sans({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-dm-sans",
})

export const metadata: Metadata = {
  title: "GitRules - Pastable powers for coding agents",
  description:
    "Augment your agents capabilities just by dropping files in your codebase. Easily add MCPs, subagents and coding guidelines to your coding context.",
  generator: "v0.app",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en" className={`${spaceGrotesk.variable} ${dmSans.variable} antialiased`}>
      <body className="font-sans">{children}</body>
    </html>
  )
}

page.tsx:
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Github, FileText, Plus, Search, Brain, Database, Code2, Zap } from "lucide-react"

export default function GitRulesLanding() {
  return (
    <div className="min-h-screen bg-pink-50">
      {/* Header */}
      <header className="border-b-4 border-black bg-white shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-cyan-400 border-2 border-black rounded-none flex items-center justify-center shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
              <Zap className="w-5 h-5 text-black" />
            </div>
            <span className="text-xl font-bold text-black">GitRules</span>
          </div>
          <nav className="flex items-center gap-6">
            <Badge className="bg-pink-400 text-black border-2 border-black shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] rounded-none font-bold">
              SOON
            </Badge>
            <span className="text-sm text-black font-medium">Docs</span>
            <Button className="bg-white text-black border-2 border-black shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] rounded-none font-bold hover:shadow-[1px_1px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[1px] hover:translate-y-[1px] transition-all">
              <Github className="w-4 h-4 mr-2" />
              GitHub
            </Button>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative py-24 px-4 bg-gradient-to-br from-pink-50 to-cyan-50">
        <div className="container mx-auto text-center max-w-4xl">
          <div className="flex items-center justify-center gap-4 mb-8">
            <div className="w-12 h-12 bg-cyan-400 border-4 border-black rounded-none flex items-center justify-center rotate-12 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
              <Zap className="w-6 h-6 text-black" />
            </div>
            <h1 className="text-5xl md:text-6xl font-black text-black leading-tight">
              Pastable powers
              <br />
              for coding agents
            </h1>
            <div className="w-12 h-12 bg-pink-400 border-4 border-black rounded-none flex items-center justify-center -rotate-12 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
              <Zap className="w-6 h-6 text-black" />
            </div>
          </div>

          <p className="text-lg text-black mb-8 max-w-2xl mx-auto leading-relaxed font-medium">
            Augment your agents capabilities just by dropping files in your codebase.
            <br />
            Easily add MCPs, subagents and coding guidelines to your coding context.
          </p>
        </div>
      </section>

      {/* Main Features Section */}
      <section className="py-20 px-4 bg-white">
        <div className="container mx-auto max-w-7xl">
          <div className="space-y-12">
            {/* Add Subagents */}
            <div className="bg-cyan-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-8">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 bg-cyan-400 border-4 border-black flex items-center justify-center">
                  <Plus className="w-6 h-6 text-black font-bold" />
                </div>
                <div>
                  <h2 className="text-3xl font-black text-black">Add Subagents</h2>
                  <p className="text-black font-medium">Enhance your workflow with specialized AI agents</p>
                </div>
              </div>

              <div className="grid md:grid-cols-2 gap-4">
                <div className="bg-white border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] p-6 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Search className="w-6 h-6 text-black" />
                    <span className="font-black text-xl text-black">Researcher</span>
                  </div>
                </div>
                <div className="bg-white border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] p-6 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Brain className="w-6 h-6 text-black" />
                    <div>
                      <div className="font-black text-xl text-black">Memory Manager</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Add MCPs */}
            <div className="bg-pink-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-8">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 bg-pink-400 border-4 border-black flex items-center justify-center">
                  <Plus className="w-6 h-6 text-black font-bold" />
                </div>
                <div>
                  <h2 className="text-3xl font-black text-black">Add MCPs</h2>
                  <p className="text-black font-medium">Integrate powerful Model Context Protocols</p>
                </div>
              </div>

              <div className="grid md:grid-cols-2 gap-4">
                <div className="bg-white border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] p-6 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Database className="w-6 h-6 text-black" />
                    <div>
                      <div className="font-black text-xl text-black">Supabase</div>
                      <div className="text-sm text-black font-bold">MCP</div>
                    </div>
                  </div>
                </div>
                <div className="bg-white border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] p-6 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Github className="w-6 h-6 text-black" />
                    <div>
                      <div className="font-black text-xl text-black">Github</div>
                      <div className="text-sm text-black font-bold">MCP</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Add Guidelines */}
            <div className="bg-cyan-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-8">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 bg-cyan-400 border-4 border-black flex items-center justify-center">
                  <Plus className="w-6 h-6 text-black font-bold" />
                </div>
                <div>
                  <h2 className="text-3xl font-black text-black">Add Guidelines</h2>
                  <p className="text-black font-medium">Define coding standards and best practices</p>
                </div>
              </div>

              <div className="grid md:grid-cols-2 gap-4">
                <div className="bg-white border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] p-6 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Code2 className="w-6 h-6 text-black" />
                    <span className="font-black text-xl text-black">Python</span>
                  </div>
                </div>
                <div className="bg-white border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] p-6 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <FileText className="w-6 h-6 text-black" />
                    <span className="font-black text-xl text-black">TypeScript</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-6 gap-4 auto-rows-fr">
            <div className="md:col-span-2 lg:col-span-2 bg-cyan-50 border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] p-6">
              <h2 className="text-2xl font-black text-black mb-4">Add Subagents</h2>
              <div className="space-y-3">
                <div className="bg-white border-2 border-black p-3 flex items-center gap-2">
                  <Search className="w-4 h-4" />
                  <span className="font-bold text-sm">Researcher</span>
                </div>
                <div className="bg-white border-2 border-black p-3 flex items-center gap-2">
                  <Brain className="w-4 h-4" />
                  <span className="font-bold text-sm">Memory Manager</span>
                </div>
              </div>
            </div>
            
            <div className="md:col-span-2 lg:col-span-2 bg-pink-50 border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] p-6">
              <h2 className="text-2xl font-black text-black mb-4">Add MCPs</h2>
              <div className="space-y-3">
                <div className="bg-white border-2 border-black p-3 flex items-center gap-2">
                  <Database className="w-4 h-4" />
                  <span className="font-bold text-sm">Supabase MCP</span>
                </div>
                <div className="bg-white border-2 border-black p-3 flex items-center gap-2">
                  <Github className="w-4 h-4" />
                  <span className="font-bold text-sm">Github MCP</span>
                </div>
              </div>
            </div>
            
            <div className="md:col-span-4 lg:col-span-2 bg-cyan-50 border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] p-6">
              <h2 className="text-2xl font-black text-black mb-4">Add Guidelines</h2>
              <div className="space-y-3">
                <div className="bg-white border-2 border-black p-3 flex items-center gap-2">
                  <Code2 className="w-4 h-4" />
                  <span className="font-bold text-sm">Python</span>
                </div>
                <div className="bg-white border-2 border-black p-3 flex items-center gap-2">
                  <FileText className="w-4 h-4" />
                  <span className="font-bold text-sm">TypeScript</span>
                </div>
              </div>
            </div>
          </div>

          <div className="space-y-8">
            <div className="text-center mb-12">
              <h2 className="text-4xl font-black text-black mb-4">Choose Your Power-Ups</h2>
              <p className="text-lg text-black font-medium">Mix and match to supercharge your coding agents</p>
            </div>
            
            <div className="grid gap-6">
              <div className="bg-gradient-to-r from-cyan-50 to-pink-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-8">
                <div className="flex flex-col md:flex-row items-start md:items-center gap-6">
                  <div className="flex-shrink-0">
                    <div className="w-16 h-16 bg-cyan-400 border-4 border-black flex items-center justify-center">
                      <Plus className="w-8 h-8 text-black font-bold" />
                    </div>
                  </div>
                  <div className="flex-grow">
                    <h3 className="text-2xl font-black text-black mb-2">Subagents</h3>
                    <p className="text-black font-medium mb-4">Specialized AI agents for different tasks</p>
                    <div className="flex flex-wrap gap-3">
                      <div className="bg-white border-2 border-black px-4 py-2 flex items-center gap-2">
                        <Search className="w-4 h-4" />
                        <span className="font-bold">Researcher</span>
                      </div>
                      <div className="bg-white border-2 border-black px-4 py-2 flex items-center gap-2">
                        <Brain className="w-4 h-4" />
                        <span className="font-bold">Memory Manager</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <div className="bg-gradient-to-r from-pink-50 to-cyan-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-8">
                <div className="flex flex-col md:flex-row items-start md:items-center gap-6">
                  <div className="flex-shrink-0">
                    <div className="w-16 h-16 bg-pink-400 border-4 border-black flex items-center justify-center">
                      <Plus className="w-8 h-8 text-black font-bold" />
                    </div>
                  </div>
                  <div className="flex-grow">
                    <h3 className="text-2xl font-black text-black mb-2">MCPs</h3>
                    <p className="text-black font-medium mb-4">Model Context Protocols for enhanced capabilities</p>
                    <div className="flex flex-wrap gap-3">
                      <div className="bg-white border-2 border-black px-4 py-2 flex items-center gap-2">
                        <Database className="w-4 h-4" />
                        <span className="font-bold">Supabase MCP</span>
                      </div>
                      <div className="bg-white border-2 border-black px-4 py-2 flex items-center gap-2">
                        <Github className="w-4 h-4" />
                        <span className="font-bold">Github MCP</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <div className="bg-gradient-to-r from-cyan-50 to-pink-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-8">
                <div className="flex flex-col md:flex-row items-start md:items-center gap-6">
                  <div className="flex-shrink-0">
                    <div className="w-16 h-16 bg-cyan-400 border-4 border-black flex items-center justify-center">
                      <Plus className="w-8 h-8 text-black font-bold" />
                    </div>
                  </div>
                  <div className="flex-grow">
                    <h3 className="text-2xl font-black text-black mb-2">Guidelines</h3>
                    <p className="text-black font-medium mb-4">Coding standards and best practices</p>
                    <div className="flex flex-wrap gap-3">
                      <div className="bg-white border-2 border-black px-4 py-2 flex items-center gap-2">
                        <Code2 className="w-4 h-4" />
                        <span className="font-bold">Python</span>
                      </div>
                      <div className="bg-white border-2 border-black px-4 py-2 flex items-center gap-2">
                        <FileText className="w-4 h-4" />
                        <span className="font-bold">TypeScript</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-cyan-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-6">
              <div className="text-center mb-6">
                <div className="w-16 h-16 bg-cyan-400 border-4 border-black mx-auto mb-4 flex items-center justify-center">
                  <Plus className="w-8 h-8 text-black font-bold" />
                </div>
                <h2 className="text-2xl font-black text-black mb-2">Add Subagents</h2>
                <p className="text-black font-medium text-sm">Specialized AI agents</p>
              </div>
              
              <div className="space-y-4">
                <div className="bg-white border-4 border-black p-4 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[-2px] hover:translate-y-[-2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Search className="w-5 h-5 text-black" />
                    <span className="font-black text-black">Researcher</span>
                  </div>
                </div>
                <div className="bg-white border-4 border-black p-4 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[-2px] hover:translate-y-[-2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Brain className="w-5 h-5 text-black" />
                    <span className="font-black text-black">Memory Manager</span>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-pink-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-6">
              <div className="text-center mb-6">
                <div className="w-16 h-16 bg-pink-400 border-4 border-black mx-auto mb-4 flex items-center justify-center">
                  <Plus className="w-8 h-8 text-black font-bold" />
                </div>
                <h2 className="text-2xl font-black text-black mb-2">Add MCPs</h2>
                <p className="text-black font-medium text-sm">Model Context Protocols</p>
              </div>
              
              <div className="space-y-4">
                <div className="bg-white border-4 border-black p-4 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[-2px] hover:translate-y-[-2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Database className="w-5 h-5 text-black" />
                    <div>
                      <div className="font-black text-black">Supabase</div>
                      <div className="text-xs text-black font-bold">MCP</div>
                    </div>
                  </div>
                </div>
                <div className="bg-white border-4 border-black p-4 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[-2px] hover:translate-y-[-2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Github className="w-5 h-5 text-black" />
                    <div>
                      <div className="font-black text-black">Github</div>
                      <div className="text-xs text-black font-bold">MCP</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-cyan-50 border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-6">
              <div className="text-center mb-6">
                <div className="w-16 h-16 bg-cyan-400 border-4 border-black mx-auto mb-4 flex items-center justify-center">
                  <Plus className="w-8 h-8 text-black font-bold" />
                </div>
                <h2 className="text-2xl font-black text-black mb-2">Add Guidelines</h2>
                <p className="text-black font-medium text-sm">Coding standards</p>
              </div>
              
              <div className="space-y-4">
                <div className="bg-white border-4 border-black p-4 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[-2px] hover:translate-y-[-2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <Code2 className="w-5 h-5 text-black" />
                    <span className="font-black text-black">Python</span>
                  </div>
                </div>
                <div className="bg-white border-4 border-black p-4 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[-2px] hover:translate-y-[-2px] transition-all cursor-pointer">
                  <div className="flex items-center gap-3">
                    <FileText className="w-5 h-5 text-black" />
                    <span className="font-black text-black">TypeScript</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t-4 border-black bg-pink-100 py-12 px-4">
        <div className="container mx-auto text-center">
          <div className="flex items-center justify-center gap-2 mb-4">
            <div className="w-6 h-6 bg-cyan-400 border-2 border-black rounded-none flex items-center justify-center shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
              <Zap className="w-4 h-4 text-black" />
            </div>
            <span className="text-lg font-black text-black">GitRules</span>
          </div>
          <p className="text-sm text-black font-medium">Empowering developers with pastable AI agent capabilities</p>
        </div>
      </footer>
    </div>
  )
}


