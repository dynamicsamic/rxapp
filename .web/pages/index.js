/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Box as RadixThemesBox, Button as RadixThemesButton, DropdownMenu as RadixThemesDropdownMenu, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Link as RadixThemesLink, Separator as RadixThemesSeparator, Text as RadixThemesText } from "@radix-ui/themes"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <RadixThemesBox>
  <RadixThemesFlex align={`start`} css={{"position": "fixed", "top": "0px", "padding": "1em", "height": "4em", "width": "100%", "zIndex": "5"}} direction={`row`} gap={`2`}>
  <RadixThemesFlex align={`start`} direction={`row`} gap={`2`}>
  <img css={{"width": "2em"}} src={`/favicon.ico`}/>
  <RadixThemesHeading css={{"fontSize": "2em"}}>
  {`Sammy sandbox`}
</RadixThemesHeading>
</RadixThemesFlex>
  <RadixThemesSeparator orientation={`vertical`} size={`4`}/>
  <RadixThemesBox>
  <RadixThemesFlex gap={`5`}>
  <RadixThemesLink asChild={true}>
  <NextLink href={`#projects`} passHref={true}>
  <RadixThemesText as={`p`} css={{"color": "var(--mauve-11)", "fontSize": "1em"}}>
  {`Projects`}
</RadixThemesText>
</NextLink>
</RadixThemesLink>
  <RadixThemesSeparator orientation={`vertical`} size={`4`}/>
  <RadixThemesLink asChild={true}>
  <NextLink href={`#stats`} passHref={true}>
  <RadixThemesText as={`p`} css={{"color": "var(--amber-7)", "fontSize": "1em"}}>
  {`Stats`}
</RadixThemesText>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
</RadixThemesBox>
  <RadixThemesFlex css={{"flex": 1, "justifySelf": "stretch", "alignSelf": "stretch"}}/>
  <RadixThemesDropdownMenu.Root>
  <RadixThemesDropdownMenu.Trigger>
  <RadixThemesButton>
  {`Menu`}
</RadixThemesButton>
</RadixThemesDropdownMenu.Trigger>
</RadixThemesDropdownMenu.Root>
</RadixThemesFlex>
  <RadixThemesFlex css={{"paddingTop": "16em", "maxWidth": "560em", "width": "100%", "marginTop": "2em", "marginBottom": "2em", "padding": "2em", "display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesBox>
  <RadixThemesHeading>
  {`Welcome to My App`}
</RadixThemesHeading>
  <RadixThemesText as={`p`}>
  {`This is the main content`}
</RadixThemesText>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesBox>
  <NextHead>
  <title>
  {`Rxapp | Index`}
</title>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
