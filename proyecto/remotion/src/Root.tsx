import React from 'react';
import {
	AbsoluteFill, Composition, Img, interpolate, spring, staticFile,
	useCurrentFrame, useVideoConfig, Easing,
} from 'remotion';

// ---------- tema ----------
const C = {
	bg: '#0d1524', bg2: '#16233a', red: '#c8102e', redSoft: '#f04a5f', white: '#f5f7fb',
	muted: '#9fb0c8', card: '#ffffff', ink: '#111827', gold: '#f2b705', wire: '#cfd8e6',
};
const FONT = 'Inter, "DejaVu Sans", sans-serif';

type Cues = Record<string, number>;
type Props = {visual: any; dur: number; cues: Cues; panel?: boolean};
const PanelCtx = React.createContext(false);

const useT = () => {
	const f = useCurrentFrame();
	const {fps} = useVideoConfig();
	return f / fps;
};
// aparición suave a partir del segundo `at`
const useIn = (at: number, len = 0.5) => {
	const f = useCurrentFrame();
	const {fps} = useVideoConfig();
	return spring({frame: f - Math.round(at * fps), fps, config: {damping: 200}, durationInFrames: Math.round(len * fps)});
};
const cueAt = (cues: Cues, c?: string, fallback = 0.3) => (c && cues[c] !== undefined ? cues[c] : fallback);

// ---------- marco común ----------
const Frame: React.FC<{heading?: string; bg?: string; children: React.ReactNode; dur: number}> = ({heading, bg, children, dur}) => {
	const t = useT();
	const head = useIn(0.05, 0.6);
	const fadeOut = interpolate(t, [dur - 0.35, dur], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	const panel = React.useContext(PanelCtx);
	return (
		<AbsoluteFill style={{background: panel ? 'transparent' : `radial-gradient(ellipse at 20% 0%, ${C.bg2} 0%, ${C.bg} 65%)`, fontFamily: FONT, color: C.white}}>
			{panel ? <Box /> : null}
			<AbsoluteFill style={{opacity: fadeOut}}>
			{bg && !panel ? (
				<AbsoluteFill>
					<Img src={staticFile(bg)} style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(22px) brightness(0.35)', transform: 'scale(1.1)'}} />
				</AbsoluteFill>
			) : null}
			<div style={{position: 'absolute', left: 96, top: 54, fontSize: 22, letterSpacing: 3, color: C.muted, textTransform: 'uppercase'}}>
				Experiencia 4 · Circuitos resistivos y ley de Ohm
			</div>
			{heading ? (
				<div style={{position: 'absolute', left: 96, top: 100, display: 'flex', alignItems: 'center', gap: 22,
					opacity: head, transform: `translateX(${(1 - head) * -40}px)`}}>
					<div style={{width: 10, height: 64, background: C.red, borderRadius: 4}} />
					<div style={{fontSize: 56, fontWeight: 700, letterSpacing: -0.5}}>{heading}</div>
				</div>
			) : null}
			<div style={{position: 'absolute', left: 96, right: 96, top: 210, bottom: panel ? 70 : 150}}>{children}</div>
			</AbsoluteFill>
		</AbsoluteFill>
	);
};
// recuadro del modo panel (se escala a 1220x686 sobre el video del grupo)
const Box: React.FC = () => (
	<AbsoluteFill style={{background: 'rgba(13,21,36,0.86)', borderRadius: 44, border: '3px solid rgba(255,255,255,0.16)',
		boxShadow: 'inset 0 0 0 1px rgba(0,0,0,0.3)'}} />
);

const Appear: React.FC<{at: number; children: React.ReactNode; style?: React.CSSProperties; dy?: number}> = ({at, children, style, dy = 24}) => {
	const p = useIn(at);
	return <div style={{opacity: p, transform: `translateY(${(1 - p) * dy}px)`, ...style}}>{children}</div>;
};

// ---------- portada / cierre ----------
const Title: React.FC<Props> = ({visual: v, dur}) => {
	const t = useT();
	const a = useIn(0.2, 0.8), b = useIn(0.7, 0.8), c = useIn(1.3, 0.8);
	const fadeOut = interpolate(t, [dur - 0.35, dur], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	const zoom = interpolate(t, [0, dur], [1.08, 1.18]);
	const panel = React.useContext(PanelCtx);
	if (panel) {
		return (
			<AbsoluteFill style={{fontFamily: FONT, color: C.white}}>
				<Box />
				<AbsoluteFill style={{opacity: fadeOut}}>
					<div style={{position: 'absolute', left: 110, top: 120, right: 110}}>
						<div style={{fontSize: 40, color: C.redSoft, fontWeight: 600, letterSpacing: 2, textTransform: 'uppercase', opacity: a}}>{v.kicker}</div>
						<div style={{fontSize: 128, fontWeight: 800, lineHeight: 1.02, marginTop: 20, letterSpacing: -2, opacity: a, transform: `translateY(${(1 - a) * 30}px)`}}>{v.title}</div>
						<div style={{width: 200, height: 10, background: C.red, borderRadius: 5, marginTop: 40, transform: `scaleX(${b})`, transformOrigin: 'left'}} />
						<div style={{marginTop: 40, fontSize: 44, lineHeight: 1.45, opacity: c, columnCount: 2, columnGap: 60}}>
							{v.members.map((m: string) => <div key={m}>{m}</div>)}
						</div>
						<div style={{marginTop: 34, fontSize: 30, color: C.muted, opacity: c}}>{v.footer}</div>
					</div>
				</AbsoluteFill>
			</AbsoluteFill>
		);
	}
	return (
		<AbsoluteFill style={{background: C.bg, fontFamily: FONT, color: C.white, opacity: fadeOut}}>
			<AbsoluteFill>
				<Img src={staticFile(v.bg)} style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(26px) brightness(0.32)', transform: `scale(${zoom})`}} />
			</AbsoluteFill>
			<AbsoluteFill style={{background: 'linear-gradient(90deg, rgba(13,21,36,0.92) 0%, rgba(13,21,36,0.55) 70%, rgba(13,21,36,0.2) 100%)'}} />
			<div style={{position: 'absolute', right: 150, top: 150, width: 420, height: 750, borderRadius: 24, overflow: 'hidden',
				boxShadow: '0 30px 80px rgba(0,0,0,0.5)', opacity: b, transform: `translateY(${(1 - b) * 30}px)`}}>
				<Img src={staticFile(v.bg)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
			</div>
			<div style={{position: 'absolute', left: 120, top: 220, width: 1150}}>
				<div style={{fontSize: 30, color: C.redSoft, fontWeight: 600, letterSpacing: 2, textTransform: 'uppercase', opacity: a}}>{v.kicker}</div>
				<div style={{fontSize: 96, fontWeight: 800, lineHeight: 1.04, marginTop: 18, letterSpacing: -1.5, opacity: a, transform: `translateY(${(1 - a) * 30}px)`}}>{v.title}</div>
				<div style={{width: 160, height: 8, background: C.red, borderRadius: 4, marginTop: 36, transform: `scaleX(${b})`, transformOrigin: 'left'}} />
				<div style={{marginTop: 40, fontSize: 32, lineHeight: 1.55, opacity: c}}>
					{v.members.map((m: string) => <div key={m}>{m}</div>)}
				</div>
				<div style={{marginTop: 34, fontSize: 22, color: C.muted, opacity: c}}>{v.footer}</div>
			</div>
		</AbsoluteFill>
	);
};

// ---------- viñetas ----------
const Bullets: React.FC<Props> = ({visual: v, dur, cues}) => (
	<Frame heading={v.heading} bg={v.bg} dur={dur}>
		{v.lead ? (
			<Appear at={cueAt(cues, v.lead.cue)} style={{fontSize: 38, lineHeight: 1.35, marginBottom: 40, maxWidth: 1500,
				borderLeft: `6px solid ${C.red}`, paddingLeft: 28}}>
				{v.lead.text}
			</Appear>
		) : null}
		<div style={{display: 'flex', gap: 60}}>
			<div style={{flex: 1}}>
				{v.items.map((it: any, i: number) => (
					<Appear key={i} at={cueAt(cues, it.cue, 0.5 + i)} style={{display: 'flex', alignItems: 'flex-start', gap: 26, marginBottom: 30}}>
						<div style={{minWidth: 52, height: 52, borderRadius: 26, background: C.red, display: 'flex', alignItems: 'center', justifyContent: 'center',
							fontSize: 26, fontWeight: 700}}>{i + 1}</div>
						<div style={{fontSize: 38, lineHeight: 1.3, paddingTop: 4}}>{it.text}</div>
					</Appear>
				))}
			</div>
			{v.eq ? (
				<Appear at={cueAt(cues, v.eq.cue)} style={{alignSelf: 'center'}}>
					<EqCard src={v.eq.src} h={110} />
				</Appear>
			) : null}
		</div>
	</Frame>
);

// ---------- ecuaciones ----------
const EqCard: React.FC<{src: string; h: number; glow?: number}> = ({src, h, glow = 0}) => (
	<div style={{background: C.card, borderRadius: 16, padding: '18px 30px', display: 'inline-block',
		boxShadow: `0 10px 30px rgba(0,0,0,0.35), 0 0 0 ${glow * 5}px rgba(200,16,46,${0.55 * glow})`}}>
		<Img src={staticFile(src)} style={{height: h, maxWidth: 800, objectFit: 'contain', objectPosition: 'left', display: 'block'}} />
	</div>
);

const Equations: React.FC<Props> = ({visual: v, dur, cues}) => {
	const t = useT();
	const eqs = v.eqs as any[];
	const n = eqs.length;
	const cols = n > 4 ? 2 : 1;
	const h = eqs[0].big ? 200 : n > 4 ? 92 : 104;
	const ats = eqs.map((e, i) => cueAt(cues, e.cue, 0.4 + i * 0.8) + (eqs.slice(0, i).filter((p) => p.cue === e.cue).length * 1.2));
	// la ecuación activa (la última que apareció) se resalta
	const active = ats.reduce((acc, a, i) => (t >= a ? i : acc), -1);
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'grid', gridTemplateColumns: `repeat(${cols}, 1fr)`, gridAutoFlow: cols === 2 ? 'column' : 'row',
				gridTemplateRows: cols === 2 ? `repeat(${Math.ceil(n / 2)}, auto)` : undefined, gap: '30px 40px', alignItems: 'start',
				justifyItems: eqs[0].big ? 'center' : 'start', marginTop: eqs[0].big ? 60 : 0}}>
				{eqs.map((e, i) => {
					const glow = active === i ? interpolate(t - ats[i], [0, 0.3], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
					return (
						<Appear key={i} at={ats[i]} dy={18}>
							<EqCard src={e.src} h={h} glow={n > 1 ? glow : 0} />
						</Appear>
					);
				})}
			</div>
			{v.note ? (
				<Appear at={cueAt(cues, v.note.cue)} style={{position: 'absolute', bottom: 0, left: 0, fontSize: 34, color: C.white,
					background: 'rgba(200,16,46,0.18)', border: `2px solid ${C.red}`, borderRadius: 14, padding: '14px 26px'}}>
					{v.note.text}
				</Appear>
			) : null}
		</Frame>
	);
};

// ---------- circuitos serie / paralelo con corriente animada ----------
const Resistor: React.FC<{x: number; y: number; vertical?: boolean; label: string}> = ({x, y, vertical, label}) => {
	const pts = [0, -14, 14, -14, 14, -14, 0].map((d, i) => (vertical ? `${x + d},${y - 60 + i * 20}` : `${x - 60 + i * 20},${y + d}`)).join(' ');
	return (
		<g>
			<polyline points={pts} fill="none" stroke={C.gold} strokeWidth={6} strokeLinejoin="round" />
			<text x={vertical ? (label.length > 3 ? x - 34 : x + 34) : x} y={vertical ? y + 10 : y - 34} fill={C.white} fontSize={30} fontWeight={700}
				textAnchor={vertical ? (label.length > 3 ? 'end' : 'start') : 'middle'} fontFamily={FONT}>{label}</text>
		</g>
	);
};
const Dots: React.FC<{d: string; len: number; speed: number; n: number}> = ({d, len, speed, n}) => {
	const t = useT();
	return (
		<path d={d} fill="none" stroke={C.redSoft} strokeWidth={9} strokeLinecap="round"
			strokeDasharray={`2 ${len / n - 2}`} strokeDashoffset={-t * speed} />
	);
};
const Circuit: React.FC<Props> = ({visual: v, dur, cues}) => {
	const serie = v.mode === 'serie';
	const draw = useIn(0.2, 1.2);
	const wire = {fill: 'none', stroke: C.wire, strokeWidth: 6};
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'flex', gap: 70, alignItems: 'flex-start'}}>
				<svg width={860} height={600} viewBox="0 0 860 600" style={{opacity: draw}}>
					{/* batería */}
					<line x1={80} y1={260} x2={80} y2={340} stroke={C.wire} strokeWidth={6} />
					<line x1={50} y1={285} x2={110} y2={285} stroke={C.white} strokeWidth={8} />
					<line x1={65} y1={315} x2={95} y2={315} stroke={C.white} strokeWidth={8} />
					<text x={20} y={250} fill={C.muted} fontSize={28} fontFamily={FONT}>10 V</text>
					{serie ? (
						<>
							<path d="M80 260 V80 H780 V520 H80 V340" {...wire} />
							<Dots d="M80 260 V80 H780 V520 H80 V340" len={2220} speed={160} n={22} />
							<rect x={170} y={60} width={140} height={40} fill={C.bg} />
							<rect x={460} y={60} width={140} height={40} fill={C.bg} />
							<rect x={760} y={230} width={40} height={140} fill={C.bg} />
							<Resistor x={240} y={80} label="R1 · 330 Ω" />
							<Resistor x={530} y={80} label="R2 · 330 Ω" />
							<Resistor x={780} y={300} vertical label="R3 · 560 Ω" />
						</>
					) : (
						<>
							<path d="M80 260 V80 H700 M80 340 V520 H700" {...wire} />
							{[300, 500, 700].map((x) => <path key={x} d={`M${x} 80 V520`} {...wire} />)}
							<Dots d="M80 260 V80 H700" len={800} speed={180} n={8} />
							<Dots d="M700 520 H80 V340" len={800} speed={180} n={8} />
							{[300, 500].map((x) => <Dots key={x} d={`M${x} 80 V520`} len={440} speed={120} n={5} />)}
							<Dots d="M700 80 V520" len={440} speed={70} n={5} />
							{[300, 500, 700].map((x) => <rect key={x} x={x - 20} y={230} width={40} height={140} fill={C.bg} />)}
							<Resistor x={300} y={300} vertical label="R1" />
							<Resistor x={500} y={300} vertical label="R2" />
							<Resistor x={700} y={300} vertical label="R3" />
						</>
					)}
				</svg>
				<div style={{flex: 1, paddingTop: 10}}>
					<Appear at={0.6}><EqCard src={v.eq} h={serie ? 70 : 90} /></Appear>
					<div style={{marginTop: 46}}>
						{v.facts.map((f: any, i: number) => (
							<Appear key={i} at={cueAt(cues, f.cue, 1 + i)} style={{fontSize: 34, lineHeight: 1.3, marginBottom: 26, display: 'flex', gap: 18}}>
								<span style={{color: C.redSoft, fontWeight: 800}}>▸</span><span>{f.text}</span>
							</Appear>
						))}
					</div>
				</div>
			</div>
		</Frame>
	);
};

// ---------- multímetro ----------
const Meter: React.FC<{kind: number}> = ({kind}) => {
	const sym = ['Ω', 'V', 'A'][kind];
	return (
		<svg width={150} height={150} viewBox="0 0 150 150">
			<rect x={25} y={10} width={100} height={130} rx={16} fill={C.gold} />
			<rect x={38} y={24} width={74} height={34} rx={5} fill="#cfe3c8" />
			<circle cx={75} cy={95} r={26} fill="#222" />
			<text x={75} y={106} fill={C.white} fontSize={30} fontWeight={800} textAnchor="middle" fontFamily={FONT}>{sym}</text>
		</svg>
	);
};
const Measure: React.FC<Props> = ({visual: v, dur, cues}) => (
	<Frame heading={v.heading} dur={dur}>
		<div style={{display: 'flex', alignItems: 'center', gap: 50}}>
			<Appear at={0.4}><EqCard src={v.eq} h={95} /></Appear>
			<Appear at={2.0} style={{fontSize: 34, lineHeight: 1.35, maxWidth: 700}}>
				Banda dorada = ±5 %: el valor real puede diferir del nominal dentro de ese margen.
			</Appear>
		</div>
		<div style={{display: 'flex', gap: 40, marginTop: 70}}>
			{v.cards.map((c: any, i: number) => (
				<Appear key={i} at={cueAt(cues, c.cue, 3 + i)} style={{flex: 1, background: 'rgba(255,255,255,0.06)', border: '1px solid rgba(255,255,255,0.14)',
					borderRadius: 22, padding: '26px 30px', display: 'flex', alignItems: 'center', gap: 22}}>
					<Meter kind={i} />
					<div>
						<div style={{fontSize: 36, fontWeight: 700, color: C.redSoft}}>{c.title}</div>
						<div style={{fontSize: 30, lineHeight: 1.3, marginTop: 8}}>{c.text}</div>
					</div>
				</Appear>
			))}
		</div>
	</Frame>
);

// ---------- tablas ----------
const Table: React.FC<Props> = ({visual: v, dur, cues}) => {
	const t = useT();
	const marks = (v.marks as any[]).map((m) => ({...m, at: cueAt(cues, m.cue)}));
	const on = (r: number, c: number) => marks.some((m) => t >= m.at && m.col === c && (m.row === undefined || m.row === r));
	return (
		<Frame heading={v.heading} dur={dur}>
			<Appear at={0.3}>
				<table style={{borderCollapse: 'separate', borderSpacing: 0, width: '100%', fontSize: 38, background: 'rgba(255,255,255,0.04)',
					borderRadius: 18, overflow: 'hidden'}}>
					<thead>
						<tr>{v.cols.map((c: string, i: number) => (
							<th key={i} style={{background: C.red, padding: '22px 26px', textAlign: i ? 'center' : 'left', fontWeight: 700, fontSize: 32}}>{c}</th>
						))}</tr>
					</thead>
					<tbody>
						{v.rows.map((r: string[], ri: number) => (
							<tr key={ri} style={{background: ri % 2 ? 'rgba(255,255,255,0.05)' : 'transparent', fontWeight: ri === v.rows.length - 1 && v.rows.length > 3 ? 700 : 400}}>
								{r.map((cell, ci) => {
									const hl = on(ri, ci);
									return (
										<td key={ci} style={{padding: '22px 26px', textAlign: ci ? 'center' : 'left', borderTop: '1px solid rgba(255,255,255,0.08)',
											color: hl ? C.ink : C.white, background: hl ? C.gold : 'transparent', fontVariantNumeric: 'tabular-nums'}}>{cell}</td>
									);
								})}
							</tr>
						))}
					</tbody>
				</table>
			</Appear>
		</Frame>
	);
};

// ---------- bombillas ----------
const Bulb: React.FC<{x: number; y: number; level: number; label: string}> = ({x, y, level, label}) => {
	const t = useT();
	const flick = 1 + 0.03 * Math.sin(t * 9 + x);
	const g = level * flick;
	return (
		<g>
			<circle cx={x} cy={y} r={70 * (0.6 + g)} fill={`rgba(255,214,90,${0.35 * g})`} />
			<circle cx={x} cy={y} r={36} fill={`rgb(${120 + 135 * g},${110 + 110 * g},${60 + 40 * g})`} stroke={C.white} strokeWidth={4} />
			<path d={`M${x - 14} ${y + 8} q7 -22 14 0 q7 22 14 0`} fill="none" stroke="#5a3b00" strokeWidth={3} />
			<text x={x} y={y + 78} fill={C.white} fontSize={30} fontWeight={700} textAnchor="middle" fontFamily={FONT}>{label}</text>
		</g>
	);
};
const Bulbs: React.FC<Props> = ({visual: v, dur, cues}) => {
	const on = useIn(1.2, 1.0); // se cierra el interruptor y encienden
	const wire = {fill: 'none', stroke: C.wire, strokeWidth: 6};
	let body: React.ReactNode;
	if (v.fig === 'a') {
		body = (<>
			<path d="M120 300 V120 H740 V480 H120 V360" {...wire} />
			<rect x={280} y={100} width={80} height={40} fill={C.bg} /><rect x={520} y={100} width={80} height={40} fill={C.bg} />
			<Bulb x={320} y={120} level={0.25 * on} label="L1 · V/2" />
			<Bulb x={560} y={120} level={0.25 * on} label="L2 · V/2" />
		</>);
	} else if (v.fig === 'b') {
		body = (<>
			<path d="M120 300 V120 H640 V480 H120 V360 M380 120 V480" {...wire} />
			<rect x={360} y={260} width={40} height={80} fill={C.bg} /><rect x={620} y={260} width={40} height={80} fill={C.bg} />
			<Bulb x={380} y={300} level={1 * on} label="L1 · V" />
			<Bulb x={640} y={300} level={1 * on} label="L2 · V" />
		</>);
	} else {
		body = (<>
			<path d="M120 300 V120 H500 M500 120 V60 H760 V120 M500 120 V180 H760 V120 M760 120 H800 V480 H120 V360" {...wire} />
			<rect x={260} y={100} width={80} height={40} fill={C.bg} /><rect x={590} y={40} width={80} height={40} fill={C.bg} /><rect x={590} y={160} width={80} height={40} fill={C.bg} />
			<Bulb x={300} y={120} level={0.45 * on} label="L1 · 2V/3" />
			<g transform="translate(0,0)">
				<Bulb x={630} y={60} level={0.11 * on} label="" />
				<Bulb x={630} y={180} level={0.11 * on} label="" />
			</g>
			<text x={830} y={70} fill={C.white} fontSize={28} fontWeight={700} fontFamily={FONT}>L2 · V/3</text>
			<text x={830} y={190} fill={C.white} fontSize={28} fontWeight={700} fontFamily={FONT}>L3 · V/3</text>
		</>);
	}
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'flex', gap: 50}}>
				<svg width={1020} height={560} viewBox="0 0 1020 560">
					<line x1={120} y1={300} x2={120} y2={360} stroke={C.wire} strokeWidth={6} />
					<line x1={90} y1={320} x2={150} y2={320} stroke={C.white} strokeWidth={8} />
					<line x1={105} y1={344} x2={135} y2={344} stroke={C.white} strokeWidth={8} />
					<text x={40} y={410} fill={C.muted} fontSize={28} fontFamily={FONT}>V</text>
					{body}
				</svg>
				<div style={{flex: 1, paddingTop: 30}}>
					{v.facts.map((f: any, i: number) => (
						<Appear key={i} at={cueAt(cues, f.cue, 1 + i)} style={{fontSize: 34, lineHeight: 1.3, marginBottom: 30, display: 'flex', gap: 18}}>
							<span style={{color: C.gold, fontWeight: 800}}>▸</span><span>{f.text}</span>
						</Appear>
					))}
				</div>
			</div>
		</Frame>
	);
};

const KINDS: Record<string, React.FC<Props>> = {title: Title, bullets: Bullets, equations: Equations, circuit: Circuit, measure: Measure, table: Table, bulbs: Bulbs};
const Slide: React.FC<Props> = (p) => {
	const K = KINDS[p.visual.kind];
	return <PanelCtx.Provider value={!!p.panel}><K {...p} /></PanelCtx.Provider>;
};

export const Root: React.FC = () => (
	<Composition id="Slide" component={Slide as any} fps={30} width={1920} height={1080} durationInFrames={150}
		defaultProps={{visual: {kind: 'title', bg: 'img/grupo.jpg', title: 'Prueba', kicker: '', members: [], footer: ''}, dur: 5, cues: {}}}
		calculateMetadata={({props}: any) => ({durationInFrames: Math.round(props.dur * 30)})} />
);
