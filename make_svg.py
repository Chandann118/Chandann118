import xml.etree.ElementTree as ET

# Read the ASCII lines
with open('ascii_final.txt', 'r', encoding='utf-8') as f:
    ascii_lines = [l.rstrip().ljust(70) for l in f.readlines()]

def create_svg(theme='dark'):
    is_dark = (theme == 'dark')
    
    # Palette definition
    if is_dark:
        bg_main_start = '#000000'
        bg_main_mid = '#000000'
        bg_main_end = '#000000'
        outer_border = '#262626'
        grid_color = '#18181B'
        grid_opacity = '0.45'
        
        card_bg = '#080808'
        card_opacity = '0.94'
        card_border_start = '#4ADE80'
        card_border_mid = '#27272A'
        card_border_end = '#18181B'
        
        inner_box_bg = '#000000'
        inner_box_border = '#262626'
        
        text_primary = '#FFFFFF'
        text_secondary = '#D4D4D8'
        text_muted = '#71717A'
        
        accent_cyan = '#4ADE80'
        accent_indigo = '#E4E4E7'
        accent_emerald = '#4ADE80'
        accent_amber = '#F59E0B'
        
        ascii_color_1 = '#FFFFFF'
        ascii_color_2 = '#E4E4E7'
        ascii_color_3 = '#4ADE80'
        
        scanline_color = '#4ADE80'
        row_highlight = '#141414'
        row_highlight_op = '0.60'
        stat_card_bg = '#000000'
        stat_card_border = '#262626'
        tag_bg = '#121212'
        tag_border = '#27272A'
    else:
        bg_main_start = '#F8FAFC'
        bg_main_mid = '#EEF6FF'
        bg_main_end = '#F1F5F9'
        outer_border = '#CBD5E1'
        grid_color = '#CBD5E1'
        grid_opacity = '0.45'
        
        card_bg = '#FFFFFF'
        card_opacity = '0.92'
        card_border_start = '#0284C7'
        card_border_mid = '#6366F1'
        card_border_end = '#CBD5E1'
        
        inner_box_bg = '#F8FAFC'
        inner_box_border = '#CBD5E1'
        
        text_primary = '#0F172A'
        text_secondary = '#475569'
        text_muted = '#64748B'
        
        accent_cyan = '#0284C7'
        accent_indigo = '#4F46E5'
        accent_emerald = '#059669'
        accent_amber = '#D97706'
        
        ascii_color_1 = '#0F172A'
        ascii_color_2 = '#1E293B'
        ascii_color_3 = '#2563EB'
        
        scanline_color = '#0284C7'
        row_highlight = '#F1F5F9'
        row_highlight_op = '0.85'
        stat_card_bg = '#F8FAFC'
        stat_card_border = '#E2E8F0'
        tag_bg = '#F1F5F9'
        tag_border = '#CBD5E1'

    # Build ASCII tspans with line-by-line reveal
    tspan_elements = []
    base_y = 117
    dy = 7.7
    for i, line in enumerate(ascii_lines):
        esc_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        delay = i * 0.025
        cur_y = base_y + i * dy
        tspan = f'          <tspan x="78" y="{cur_y:.2f}" opacity="0">{esc_line}<animate attributeName="opacity" from="0" to="1" dur="0.2s" begin="{delay:.3f}s" fill="freeze"/></tspan>'
        tspan_elements.append(tspan)
    tspans_str = '\n'.join(tspan_elements)

    glow_left_op = '0.08' if is_dark else '0.08'
    glow_right_op = '0.05' if is_dark else '0.08'

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610" role="img" aria-label="Chandan Yadav (Yashu) - Developer Profile Banner">
  <defs>
    <!-- Gradients -->
    <linearGradient id="bg-grad-{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_main_start}"/>
      <stop offset="50%" stop-color="{bg_main_mid}"/>
      <stop offset="100%" stop-color="{bg_main_end}"/>
    </linearGradient>

    <linearGradient id="border-grad-{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{card_border_start}" stop-opacity="0.75"/>
      <stop offset="45%" stop-color="{card_border_mid}" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="{card_border_end}" stop-opacity="0.3"/>
    </linearGradient>

    <linearGradient id="ascii-grad-{theme}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{ascii_color_1}"/>
      <stop offset="45%" stop-color="{ascii_color_2}"/>
      <stop offset="100%" stop-color="{ascii_color_3}"/>
    </linearGradient>

    <linearGradient id="scanline-{theme}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{scanline_color}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{scanline_color}" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="{scanline_color}" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="accent-text-{theme}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_cyan}"/>
      <stop offset="100%" stop-color="{accent_indigo}"/>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="grid-{theme}" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_color}" stroke-width="0.8" stroke-opacity="{grid_opacity}"/>
    </pattern>

    <!-- Ambient Glow Filters -->
    <radialGradient id="glow-left-{theme}" cx="15%" cy="15%" r="45%">
      <stop offset="0%" stop-color="{accent_cyan}" stop-opacity="{glow_left_op}"/>
      <stop offset="100%" stop-color="{accent_cyan}" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="glow-right-{theme}" cx="85%" cy="20%" r="50%">
      <stop offset="0%" stop-color="{accent_indigo}" stop-opacity="{glow_right_op}"/>
      <stop offset="100%" stop-color="{accent_indigo}" stop-opacity="0"/>
    </radialGradient>

    <clipPath id="rounded-frame">
      <rect x="10" y="10" width="1160" height="590" rx="20" ry="20"/>
    </clipPath>
    
    <clipPath id="portrait-clip">
      <rect x="42" y="98" width="382" height="348" rx="10" ry="10"/>
    </clipPath>
  </defs>

  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .ascii-text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace; font-size: 6.85px; font-weight: 600; letter-spacing: 0.25px; }}
  </style>

  <!-- Frame & Background -->
  <g clip-path="url(#rounded-frame)">
    <rect x="10" y="10" width="1160" height="590" rx="20" fill="url(#bg-grad-{theme})" stroke="{outer_border}" stroke-width="1.5"/>
    <rect x="10" y="10" width="1160" height="590" fill="url(#grid-{theme})"/>
    <circle cx="180" cy="160" r="320" fill="url(#glow-left-{theme})"/>
    <circle cx="980" cy="180" r="350" fill="url(#glow-right-{theme})"/>

    <!-- Ambient Floating Particles (SMIL) -->
    <circle cx="220" cy="80" r="1.8" fill="{accent_cyan}" opacity="0.6">
      <animate attributeName="cy" values="80;70;80" dur="5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.3;0.8;0.3" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="640" cy="50" r="1.5" fill="{accent_indigo}" opacity="0.5">
      <animate attributeName="cy" values="50;60;50" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.2;0.7;0.2" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1060" cy="90" r="1.6" fill="{accent_emerald}" opacity="0.5">
      <animate attributeName="cy" values="90;82;90" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.3;0.8;0.3" dur="7s" repeatCount="indefinite"/>
    </circle>

    <!-- Top Navigation Chrome -->
    <g id="header-chrome">
      <!-- Traffic Light Controls -->
      <circle cx="36" cy="35" r="5.5" fill="#EF4444"/>
      <circle cx="54" cy="35" r="5.5" fill="#F59E0B"/>
      <circle cx="72" cy="35" r="5.5" fill="#10B981"/>

      <!-- Prompt Host -->
      <text x="100" y="39" class="mono" font-size="12" font-weight="600" fill="{text_secondary}">
        chandann118<tspan fill="{accent_cyan}">@terminal</tspan><tspan fill="{text_muted}">:~#</tspan> profile --inspect
      </text>

      <!-- Center Title Tag -->
      <text x="590" y="39" class="mono" font-size="11" font-weight="600" text-anchor="middle" fill="{text_muted}" letter-spacing="1.5px">
        CHANDAN YADAV (YASHU) // DEVELOPER IDENTITY MATRIX
      </text>

      <!-- Right Telemetry Badges -->
      <g transform="translate(880, 23)">
        <!-- Live Beacon -->
        <rect x="0" y="0" width="86" height="24" rx="12" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
        <circle cx="14" cy="12" r="4" fill="{accent_emerald}">
          <animate attributeName="r" values="3.5;5;3.5" dur="2s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
        </circle>
        <text x="26" y="16" class="mono" font-size="9.5" font-weight="700" fill="{text_primary}">ONLINE</text>

        <!-- Degree Badge -->
        <rect x="94" y="0" width="88" height="24" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
        <text x="138" y="16" class="mono" font-size="9.5" font-weight="600" text-anchor="middle" fill="{accent_cyan}">B.TECH IT</text>

        <!-- Framework Badge -->
        <rect x="190" y="0" width="88" height="24" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
        <text x="234" y="16" class="mono" font-size="9.5" font-weight="600" text-anchor="middle" fill="{accent_emerald}">SPRING BOOT</text>
      </g>

      <!-- Divider line below chrome -->
      <line x1="10" y1="55" x2="1170" y2="55" stroke="{outer_border}" stroke-width="1" opacity="0.7"/>
    </g>

    <!-- ==================== LEFT COLUMN: VISUAL IDENTITY ==================== -->
    <g id="left-panel">
      <!-- Left Card Container -->
      <rect x="26" y="68" width="414" height="514" rx="14" fill="{card_bg}" fill-opacity="{card_opacity}" stroke="url(#border-grad-{theme})" stroke-width="1.2"/>

      <!-- Left Header -->
      <text x="44" y="89" class="mono" font-size="11" font-weight="700" fill="{accent_cyan}" letter-spacing="1.2px">// VISUAL.MAP</text>
      <text x="165" y="89" class="mono" font-size="10" fill="{text_muted}">ASCII_SCAN: 70x42 MATRIX</text>
      <rect x="350" y="78" width="74" height="18" rx="4" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
      <text x="387" y="90.5" class="mono" font-size="8.5" font-weight="700" text-anchor="middle" fill="{accent_emerald}">RENDERED</text>

      <!-- Inner ASCII Box -->
      <g clip-path="url(#portrait-clip)">
        <rect x="42" y="98" width="382" height="348" rx="10" fill="{inner_box_bg}" stroke="{inner_box_border}" stroke-width="1"/>

        <!-- Subtle Inner Grid Lines -->
        <line x1="42" y1="185" x2="424" y2="185" stroke="{grid_color}" stroke-width="0.5" stroke-opacity="0.3" stroke-dasharray="4 4"/>
        <line x1="42" y1="272" x2="424" y2="272" stroke="{grid_color}" stroke-width="0.5" stroke-opacity="0.3" stroke-dasharray="4 4"/>
        <line x1="42" y1="359" x2="424" y2="359" stroke="{grid_color}" stroke-width="0.5" stroke-opacity="0.3" stroke-dasharray="4 4"/>
        <line x1="169" y1="98" x2="169" y2="446" stroke="{grid_color}" stroke-width="0.5" stroke-opacity="0.3" stroke-dasharray="4 4"/>
        <line x1="296" y1="98" x2="296" y2="446" stroke="{grid_color}" stroke-width="0.5" stroke-opacity="0.3" stroke-dasharray="4 4"/>

        <!-- Floating Portrait Container -->
        <g id="ascii-portrait-group">
          <animateTransform attributeName="transform" type="translate" values="0,0; 0,-2.5; 0,0" dur="7s" repeatCount="indefinite"/>
          <text class="ascii-text" fill="url(#ascii-grad-{theme})" xml:space="preserve">
{tspans_str}
          </text>
        </g>

        <!-- Horizontal Laser Scanline (SMIL) -->
        <line x1="42" y1="98" x2="424" y2="98" stroke="url(#scanline-{theme})" stroke-width="2">
          <animate attributeName="y1" values="98;446;98" dur="6s" repeatCount="indefinite"/>
          <animate attributeName="y2" values="98;446;98" dur="6s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="0.3;0.8;0.3" dur="6s" repeatCount="indefinite"/>
        </line>

        <!-- HUD Corner Brackets -->
        <path d="M 48 112 L 48 104 L 56 104" fill="none" stroke="{accent_cyan}" stroke-width="1.8" opacity="0.8"/>
        <path d="M 418 112 L 418 104 L 410 104" fill="none" stroke="{accent_cyan}" stroke-width="1.8" opacity="0.8"/>
        <path d="M 48 432 L 48 440 L 56 440" fill="none" stroke="{accent_cyan}" stroke-width="1.8" opacity="0.8"/>
        <path d="M 418 432 L 418 440 L 410 440" fill="none" stroke="{accent_cyan}" stroke-width="1.8" opacity="0.8"/>
      </g>

      <!-- Bottom Identity Area in Left Panel -->
      <g transform="translate(44, 460)">
        <line x1="0" y1="0" x2="378" y2="0" stroke="{outer_border}" stroke-width="1" opacity="0.7"/>

        <!-- Command Prompt Line -->
        <text x="0" y="18" class="mono" font-size="11" fill="{text_muted}">
          <tspan fill="{accent_cyan}">chandann118@dev</tspan>:~$ whoami
        </text>

        <!-- Large Name & Nickname -->
        <text x="0" y="43" class="sans" font-size="20" font-weight="800" fill="{text_primary}" letter-spacing="-0.4px">
          Chandan Yadav <tspan font-size="13" font-weight="600" fill="{accent_cyan}">[Yashu]</tspan>
        </text>

        <!-- Dynamic Rotating Role (SMIL) -->
        <g transform="translate(0, 65)">
          <text class="mono" font-size="12" font-weight="600">
            <tspan fill="{accent_cyan}" opacity="1">
              Student · B.Tech IT
              <animate attributeName="opacity" values="1;1;0;0;0;0;1" dur="9s" repeatCount="indefinite"/>
            </tspan>
            <tspan x="0" y="0" fill="{accent_emerald}" opacity="0">
              Backend Developer · Spring Boot
              <animate attributeName="opacity" values="0;0;1;1;0;0;0" dur="9s" repeatCount="indefinite"/>
            </tspan>
            <tspan x="0" y="0" fill="{accent_indigo}" opacity="0">
              Problem Solver · LeetCode DSA
              <animate attributeName="opacity" values="0;0;0;0;1;1;0" dur="9s" repeatCount="indefinite"/>
            </tspan>
            <tspan fill="{accent_cyan}">_
              <animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/>
            </tspan>
          </text>
        </g>

        <!-- Subtext Status Badges -->
        <g transform="translate(0, 88)">
          <rect x="0" y="0" width="145" height="22" rx="5" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
          <circle cx="10" cy="11" r="3" fill="{accent_emerald}"/>
          <text x="19" y="14.5" class="mono" font-size="9" font-weight="600" fill="{text_secondary}">JVM Backends</text>

          <rect x="153" y="0" width="155" height="22" rx="5" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
          <circle cx="163" cy="11" r="3" fill="{accent_cyan}"/>
          <text x="172" y="14.5" class="mono" font-size="9" font-weight="600" fill="{text_secondary}">DSA &amp; Problem Solving</text>
        </g>
      </g>
    </g>

    <!-- ==================== RIGHT COLUMN: SYSTEM INFO ==================== -->
    <g id="right-panel">
      <!-- Right Card Container -->
      <rect x="454" y="68" width="700" height="514" rx="14" fill="{card_bg}" fill-opacity="{card_opacity}" stroke="url(#border-grad-{theme})" stroke-width="1.2"/>

      <!-- Right Header -->
      <text x="474" y="89" class="mono" font-size="11" font-weight="700" fill="{accent_cyan}" letter-spacing="1.2px">// SYSTEM.INFO</text>
      <text x="595" y="89" class="mono" font-size="10" fill="{text_muted}">./profile.sh --fetch-all</text>
      <rect x="1066" y="78" width="68" height="18" rx="4" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
      <text x="1100" y="90.5" class="mono" font-size="8.5" font-weight="700" text-anchor="middle" fill="{accent_cyan}">STATUS: OK</text>

      <line x1="454" y1="102" x2="1154" y2="102" stroke="{outer_border}" stroke-width="1" opacity="0.6"/>

      <!-- SECTION 1: SYSTEM ATTRIBUTES (TABLE) -->
      <g id="profile-table" transform="translate(474, 108)">
        <!-- Table rows with alternating zebra strips -->
        <!-- Row 1: NAME -->
        <rect x="0" y="2" width="660" height="20" rx="4" fill="{row_highlight}" fill-opacity="{row_highlight_op}"/>
        <text x="10" y="16" class="mono" font-size="10" font-weight="700" fill="{accent_cyan}">&gt; IDENTIFIER  :</text>
        <text x="145" y="16" class="mono" font-size="11" font-weight="700" fill="{text_primary}">Chandan Yadav</text>
        <text x="250" y="16" class="mono" font-size="10" font-weight="600" fill="{accent_cyan}">[aka: Yashu]</text>
        <text x="540" y="16" class="mono" font-size="9" fill="{text_muted}">[VERIFIED PROFILE]</text>

        <!-- Row 2: HEADLINE -->
        <text x="10" y="37" class="mono" font-size="10" font-weight="700" fill="{accent_cyan}">&gt; HEADLINE    :</text>
        <text x="145" y="37" class="mono" font-size="11" font-weight="600" fill="{text_secondary}">Student // B.Tech IT</text>
        <text x="540" y="37" class="mono" font-size="9" fill="{accent_indigo}">[ACADEMICS]</text>

        <!-- Row 3: BACKEND -->
        <rect x="0" y="44" width="660" height="20" rx="4" fill="{row_highlight}" fill-opacity="{row_highlight_op}"/>
        <text x="10" y="58" class="mono" font-size="10" font-weight="700" fill="{accent_cyan}">&gt; BACKEND TECH:</text>
        <text x="145" y="58" class="mono" font-size="11" font-weight="700" fill="{accent_emerald}">Spring Boot</text>
        <text x="245" y="58" class="mono" font-size="10.5" fill="{text_secondary}">· Java Enterprise Architecture</text>
        <text x="540" y="58" class="mono" font-size="9" fill="{accent_emerald}">[SPECIALIZATION]</text>

        <!-- Row 4: LEETCODE -->
        <text x="10" y="79" class="mono" font-size="10" font-weight="700" fill="{accent_cyan}">&gt; LEETCODE    :</text>
        <text x="145" y="79" class="mono" font-size="11" font-weight="600" fill="{text_primary}">Chandann118</text>
        <text x="245" y="79" class="mono" font-size="10.5" fill="{text_secondary}">· Data Structures &amp; Algorithms</text>
        <text x="540" y="79" class="mono" font-size="9" fill="{accent_amber}">[PROBLEM SOLVING]</text>

        <!-- Row 5: EDUCATION -->
        <rect x="0" y="86" width="660" height="20" rx="4" fill="{row_highlight}" fill-opacity="{row_highlight_op}"/>
        <text x="10" y="100" class="mono" font-size="10" font-weight="700" fill="{accent_cyan}">&gt; EDUCATION   :</text>
        <text x="145" y="100" class="mono" font-size="11" font-weight="600" fill="{text_primary}">B.Tech (IT)</text>
        <text x="235" y="100" class="mono" font-size="10.5" fill="{text_secondary}">· Information Technology</text>
        <text x="540" y="100" class="mono" font-size="9" fill="{accent_cyan}">[UNDERGRAD]</text>

        <!-- Row 6: GITHUB -->
        <text x="10" y="121" class="mono" font-size="10" font-weight="700" fill="{accent_cyan}">&gt; REPOSITORY  :</text>
        <text x="145" y="121" class="mono" font-size="11" font-weight="600" fill="{text_primary}">github.com/Chandann118/Chandann118</text>
        <text x="540" y="121" class="mono" font-size="9" fill="{accent_indigo}">[MAIN REPO]</text>

        <!-- Row 7: CONTACT -->
        <rect x="0" y="128" width="660" height="20" rx="4" fill="{row_highlight}" fill-opacity="{row_highlight_op}"/>
        <text x="10" y="142" class="mono" font-size="10" font-weight="700" fill="{accent_cyan}">&gt; CONTACT     :</text>
        <text x="145" y="142" class="mono" font-size="11" font-weight="600" fill="{text_primary}">chandnn188@gmail.com</text>
        <text x="540" y="142" class="mono" font-size="9" fill="{accent_emerald}">[OPEN TO CONNECT]</text>
      </g>

      <line x1="474" y1="266" x2="1134" y2="266" stroke="{outer_border}" stroke-width="1" opacity="0.6"/>

      <!-- SECTION 2: TECH STACK PILLS -->
      <g id="tech-stack" transform="translate(474, 276)">
        <text x="0" y="13" class="mono" font-size="10.5" font-weight="700" fill="{accent_cyan}" letter-spacing="1px">
          // CORE TECHNICAL FOCUS &amp; DISCIPLINES
        </text>

        <g transform="translate(0, 24)">
          <!-- Pill 1: Spring Boot -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="130" height="28" rx="6" fill="{tag_bg}" stroke="{accent_emerald}" stroke-width="1.2"/>
            <circle cx="14" cy="14" r="3.5" fill="{accent_emerald}"/>
            <text x="25" y="18" class="mono" font-size="10.5" font-weight="700" fill="{text_primary}">Spring Boot</text>
          </g>

          <!-- Pill 2: Java -->
          <g transform="translate(140, 0)">
            <rect x="0" y="0" width="100" height="28" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <circle cx="14" cy="14" r="3.5" fill="{accent_cyan}"/>
            <text x="25" y="18" class="mono" font-size="10.5" font-weight="600" fill="{text_primary}">Java Core</text>
          </g>

          <!-- Pill 3: DSA -->
          <g transform="translate(250, 0)">
            <rect x="0" y="0" width="160" height="28" rx="6" fill="{tag_bg}" stroke="{accent_amber}" stroke-width="1.2"/>
            <circle cx="14" cy="14" r="3.5" fill="{accent_amber}"/>
            <text x="25" y="18" class="mono" font-size="10.5" font-weight="700" fill="{text_primary}">Data Structures</text>
          </g>

          <!-- Pill 4: LeetCode -->
          <g transform="translate(420, 0)">
            <rect x="0" y="0" width="125" height="28" rx="6" fill="{tag_bg}" stroke="{accent_amber}" stroke-width="1"/>
            <circle cx="14" cy="14" r="3.5" fill="{accent_amber}"/>
            <text x="25" y="18" class="mono" font-size="10.5" font-weight="600" fill="{text_primary}">LeetCode</text>
          </g>

          <!-- Pill 5: REST APIs -->
          <g transform="translate(555, 0)">
            <rect x="0" y="0" width="105" height="28" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <circle cx="14" cy="14" r="3.5" fill="{accent_indigo}"/>
            <text x="25" y="18" class="mono" font-size="10.5" font-weight="600" fill="{text_primary}">REST APIs</text>
          </g>

          <!-- Row 2 Pills -->
          <g transform="translate(0, 36)">
            <!-- Pill 6: Backend Systems -->
            <rect x="0" y="0" width="155" height="26" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <circle cx="14" cy="13" r="3" fill="{accent_cyan}"/>
            <text x="25" y="16.5" class="mono" font-size="10" font-weight="600" fill="{text_secondary}">Backend Systems</text>

            <!-- Pill 7: Algorithms -->
            <rect x="165" y="0" width="155" height="26" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <circle cx="179" cy="13" r="3" fill="{accent_indigo}"/>
            <text x="190" y="16.5" class="mono" font-size="10" font-weight="600" fill="{text_secondary}">Algorithm Design</text>

            <!-- Pill 8: Git & GitHub -->
            <rect x="330" y="0" width="140" height="26" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <circle cx="344" cy="13" r="3" fill="{accent_emerald}"/>
            <text x="355" y="16.5" class="mono" font-size="10" font-weight="600" fill="{text_secondary}">Git &amp; GitHub</text>

            <!-- Pill 9: Engineering -->
            <rect x="480" y="0" width="180" height="26" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <circle cx="494" cy="13" r="3" fill="{accent_cyan}"/>
            <text x="505" y="16.5" class="mono" font-size="10" font-weight="600" fill="{text_secondary}">Information Tech B.Tech</text>
          </g>
        </g>
      </g>

      <line x1="474" y1="375" x2="1134" y2="375" stroke="{outer_border}" stroke-width="1" opacity="0.6"/>

      <!-- SECTION 3: ENGINEERING TELEMETRY CARDS -->
      <g id="telemetry-cards" transform="translate(474, 386)">
        <!-- Card 1: Backend Architecture -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="212" height="66" rx="8" fill="{stat_card_bg}" stroke="{stat_card_border}" stroke-width="1"/>
          <text x="14" y="19" class="mono" font-size="9" font-weight="700" fill="{accent_emerald}" letter-spacing="0.5px">CORE SPECIALTY</text>
          <text x="14" y="39" class="sans" font-size="15" font-weight="700" fill="{text_primary}">Spring Boot</text>
          <text x="14" y="54" class="mono" font-size="9.5" fill="{text_muted}">JVM Backend &amp; Services</text>
        </g>

        <!-- Card 2: LeetCode & Algorithms -->
        <g transform="translate(224, 0)">
          <rect x="0" y="0" width="212" height="66" rx="8" fill="{stat_card_bg}" stroke="{stat_card_border}" stroke-width="1"/>
          <text x="14" y="19" class="mono" font-size="9" font-weight="700" fill="{accent_amber}" letter-spacing="0.5px">PROBLEM SOLVING</text>
          <text x="14" y="39" class="sans" font-size="15" font-weight="700" fill="{text_primary}">LeetCode Profile</text>
          <text x="14" y="54" class="mono" font-size="9.5" fill="{text_muted}">u/Chandann118</text>
        </g>

        <!-- Card 3: Academic Path -->
        <g transform="translate(448, 0)">
          <rect x="0" y="0" width="212" height="66" rx="8" fill="{stat_card_bg}" stroke="{stat_card_border}" stroke-width="1"/>
          <text x="14" y="19" class="mono" font-size="9" font-weight="700" fill="{accent_cyan}" letter-spacing="0.5px">ACADEMIC STATUS</text>
          <text x="14" y="39" class="sans" font-size="15" font-weight="700" fill="{text_primary}">B.Tech (IT)</text>
          <text x="14" y="54" class="mono" font-size="9.5" fill="{text_muted}">Information Technology</text>
        </g>
      </g>

      <line x1="474" y1="462" x2="1134" y2="462" stroke="{outer_border}" stroke-width="1" opacity="0.6"/>

      <!-- SECTION 4: DIRECT LINKS & TERMINAL EXECUTION -->
      <g id="connect-links" transform="translate(474, 472)">
        <text x="0" y="13" class="mono" font-size="10.5" font-weight="700" fill="{accent_cyan}" letter-spacing="1px">
          // ACTIVE CHANNELS &amp; REPOSITORIES
        </text>

        <!-- 5 Badges in a Row -->
        <g transform="translate(0, 22)">
          <!-- GitHub Link Pill -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="126" height="28" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <text x="10" y="18" class="mono" font-size="9.5" font-weight="700" fill="{accent_cyan}">GitHub</text>
            <text x="54" y="18" class="mono" font-size="9" fill="{text_secondary}">Chandann118</text>
          </g>

          <!-- LinkedIn Link Pill -->
          <g transform="translate(133, 0)">
            <rect x="0" y="0" width="126" height="28" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <text x="10" y="18" class="mono" font-size="9.5" font-weight="700" fill="{accent_indigo}">LinkedIn</text>
            <text x="60" y="18" class="mono" font-size="9" fill="{text_secondary}">chandann118</text>
          </g>

          <!-- LeetCode Link Pill -->
          <g transform="translate(266, 0)">
            <rect x="0" y="0" width="126" height="28" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <text x="10" y="18" class="mono" font-size="9.5" font-weight="700" fill="{accent_amber}">LeetCode</text>
            <text x="62" y="18" class="mono" font-size="9" fill="{text_secondary}">Chandann118</text>
          </g>

          <!-- Instagram Link Pill -->
          <g transform="translate(399, 0)">
            <rect x="0" y="0" width="128" height="28" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <text x="10" y="18" class="mono" font-size="9.5" font-weight="700" fill="#E1306C">Instagram</text>
            <text x="68" y="18" class="mono" font-size="9" fill="{text_secondary}">chandann118</text>
          </g>

          <!-- Email Link Pill -->
          <g transform="translate(534, 0)">
            <rect x="0" y="0" width="126" height="28" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <text x="10" y="18" class="mono" font-size="9.5" font-weight="700" fill="{accent_emerald}">Email</text>
            <text x="46" y="18" class="mono" font-size="8.8" fill="{text_secondary}">chandnn188</text>
          </g>
        </g>

        <!-- Bottom Bash Execution Bar -->
        <g transform="translate(0, 64)">
          <rect x="0" y="0" width="660" height="26" rx="5" fill="{inner_box_bg}" stroke="{inner_box_border}" stroke-width="1"/>
          <text x="12" y="17" class="mono" font-size="10.5" fill="{text_muted}">
            <tspan fill="{accent_cyan}">chandann118@server</tspan>:~$ echo &quot;Developing robust Spring Boot backends &amp; solving algorithms.&quot;
            <tspan fill="{accent_emerald}">_
              <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
            </tspan>
          </text>
        </g>
      </g>
    </g>
  </g>
</svg>'''
    return svg

# Test parsing both SVGs
dark_svg = create_svg('dark')
light_svg = create_svg('light')

ET.fromstring(dark_svg)
print('Dark SVG parsed successfully! Size:', len(dark_svg))

ET.fromstring(light_svg)
print('Light SVG parsed successfully! Size:', len(light_svg))

with open('dark.svg', 'w', encoding='utf-8') as f:
    f.write(dark_svg)

with open('light.svg', 'w', encoding='utf-8') as f:
    f.write(light_svg)

print('dark.svg and light.svg written to disk!')
